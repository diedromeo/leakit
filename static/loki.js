console.log("%cLoki's Trickery: TVA Secured System", "color: lime; font-size: 16px; font-weight: bold; background: black; padding: 4px;");

fetch('/api/versions/2')
    .then(response => response.json())
    .then(data => {
        console.log("%cAPI Response:", "color: yellow; font-weight: bold;");
        console.log(data);
    })
    .catch(error => console.error('API error:', error));