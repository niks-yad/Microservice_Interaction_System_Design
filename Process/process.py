from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Process Service: Converting your videos to audio!'

if __name__ == '__main__':
    app.run(debug=True, port=5004)
