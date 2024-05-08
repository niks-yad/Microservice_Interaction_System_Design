from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Upload Service on port 5002: Ready to receive videos!'

if __name__ == '__main__':
    app.run(debug=True, port=5002)
