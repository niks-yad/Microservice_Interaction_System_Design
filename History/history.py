from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'History Service: Track your past conversions!'

if __name__ == '__main__':
    app.run(debug=True, port=5005)
