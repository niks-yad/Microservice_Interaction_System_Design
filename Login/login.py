from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Login Service: Welcome to the Video to Audio Converter App!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use a unique port for each service
