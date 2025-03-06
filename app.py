from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

FLAG = "byteme{t1m3_st0n3s_t4ke_y0u_b4ck}"

@app.route('/')
def home():
    return render_template("index.html")  # Main Page

@app.route('/api/versions/2')
def api_v2():
    return jsonify({
        "version": "2.0",
        "message": "Welcome to Loki’s new secured API. Nothing to see here.",
        "status": "Protected",
        "data": {
            "token": "XV-92A-LOCK",
            "info": "System secured under TVA jurisdiction."
        }
    })

@app.route('/api/versions/1')
def api_v1():
    return jsonify({
        "version": "1.0",
        "flag": FLAG
    })

if __name__ == '__main__':
    app.run(debug=True)

