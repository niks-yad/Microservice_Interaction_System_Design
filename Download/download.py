from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Download Service on port 5003: Download your audio files here'

if __name__ == '__main__':
    app.run(debug=True, port=5003)
