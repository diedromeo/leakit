from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from uuid import uuid4

app = Flask(__name__)
app.secret_key = 'one-piece-flag-secret'

users_db = {}
ranks_allowed = ['cadet', 'marine', 'viceAdmiral']
admin_role = 'fleetAdmiral'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html', ranks=ranks_allowed)

@app.route('/api/register', methods=['POST'])
def register_api():
    data = request.get_json()
    attributes = data.get('attributes', {})
    relationships = data.get('relationships', {})
    ranks = relationships.get('ranks', {}).get('data', [])

    user_id = str(uuid4())
    email = attributes.get('email')
    mission_reason = attributes.get('missionReason')
    status = attributes.get('status', 'pending')

    rank_id = 'cadet'
    if ranks:
        rank_id = ranks[0].get('id', 'cadet')

    users_db[email] = {
        'id': user_id,
        'email': email,
        'missionReason': mission_reason,
        'status': status,
        'rank': rank_id
    }

    return jsonify({
        'message': 'Registration created',
        'status': status,
        'user_id': user_id
    }), 201

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        user = users_db.get(email)
        if user and user['status'] == 'approved':
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Access Denied. Await approval from Marine HQ.")
    return render_template('login.html')

@app.route('/marine-admin')
def dashboard():
    email = session.get('user')
    if not email or email not in users_db:
        return redirect(url_for('login'))
    user = users_db[email]
    if user['rank'] != admin_role:
        return "⚠️ Access Denied. Only the Fleet Admiral can enter here.", 403
    return render_template('admin.html', flag="CTF{straw_hat_admin_bypass}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
