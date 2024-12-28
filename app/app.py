from flask import Flask, session, request
from flask_cors import CORS
from flask_session import Session
from SessionChat import SessionChat


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
CORS(app)


@app.route("/hello", methods=["PUT"])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/start_session", methods=["GET"])
def start_session():
    session["SessionChat"] = SessionChat()
    return ""


@app.route("/add_comment", methods=["GET"])
def add_comment():
    member_name = request.args.get("member_name")
    comment = request.args.get("comment")
    if "SessionChat" in session:
        session["SessionChat"].register_comment(member_name, comment)
        return "Comment added"
    else:
        return "No active session", 400
    
@app.route("/comments_table", methods=["GET"])
def comments_table():
    if "SessionChat" in session:
        return session["SessionChat"].get_comments_table()
    else:
        return "No active session", 400