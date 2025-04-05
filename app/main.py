import os
from flask import Flask, jsonify
from logic import fetch_all_characters, filter_characters

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Rick and Morty Character Filter</h1>
    <p>Use the following endpoints:</p>
    <ul>
        <li><a href="/healthcheck">/healthcheck</a> – Check service health</li>
        <li><a href="/characters">/characters</a> – Get alive humans from Earth</li>
    </ul>
    '''

@app.route('/healthcheck')
def healthcheck():
    return jsonify({"status": "ok"})

@app.route('/characters')
def get_characters():
    all_chars = fetch_all_characters()
    filtered = filter_characters(all_chars)
    return jsonify(filtered)

if __name__ == '__main__':
    host = os.getenv('APP_HOST', '0.0.0.0')
    port = int(os.getenv('APP_PORT', 5000))
    app.run(host=host, port=port)
