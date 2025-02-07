from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/love')
def love():
    return render_template('love.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
