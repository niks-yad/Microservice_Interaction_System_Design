from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from flaskext.mysql import MySQL

# adding comments
# in this file

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-value'  # Change this to an actual value..
app.config['MYSQL_DATABASE_USER'] = 'user' # is this gonna be a variable...?
app.config['MYSQL_DATABASE_PASSWORD'] = 'password' # this i know
app.config['MYSQL_DATABASE_DB'] = 'user_db' # this 
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from users where username=%s and password=%s", (username, password))
    data = cursor.fetchone()
    if data is None:
        return jsonify({"msg": "Bad username or password"}), 401 # as in error 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    cursor = mysql.connect().cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    mysql.connect().commit()
    return jsonify({"msg": "User created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
