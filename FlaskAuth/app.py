from flask import Flask, request, jsonify
from models.user import User
import bcrypt
from database import db
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    logout_user,
    login_required,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root@127.0.0.1:3306/flask_crud"  # Replace with your own database URI
)


login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
# View Login
login_manager.login_view = "login"

# Session


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Authentication completed "})

    return jsonify({"message": "Invalid credentials"}), 400


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout completed"})


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(username=username, password=hashed_password, role="user")
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201

    return jsonify({"message": "Invalid credentials"}), 401


@app.route("/user/<int:id_user>", methods=["GET"])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)
    if user:
        return {"username": user.username}

    return jsonify({"message": "User not found"}), 404


@app.route("/user/<int:id_user>", methods=["PUT"])
@login_required
def update_user(id_user):
    data = request.json
    user = User.query.get(id_user)

    if id_user != current_user.id and current_user.role == "user":
        return jsonify({"message": "You can't update other users"}), 403

    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()

        return {"message": f"User {id_user} updated"}

    return jsonify({"message": "User not found"}), 404


@app.route("/user/<int:id_user>", methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if current_user.role != 'admin':
        return jsonify({"message": "You don't have permission to delete users"}), 403
    
    if id_user == current_user.id:
        return jsonify({"message": "You can't delete your own user"}), 403

    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {id_user} deleted"}

    return jsonify({"message": "User not found"}), 404


@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
