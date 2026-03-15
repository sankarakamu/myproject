from flask import Flask,request,jsonify
from flask import send_from_directory
import sqlite3

app = Flask(__name__)
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

def get_db():
    conn = sqlite3.connect("issues.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/report",methods=["POST"])
def report_issue():

    data=request.json

    username=data["username"]
    title=data["title"]
    category=data["category"]
    description=data["description"]
    location=data["location"]

    conn=get_db()
    cur=conn.cursor()

    cur.execute(
    "INSERT INTO issues (username,title,category,description,location) VALUES (?,?,?,?,?)",
    (username,title,category,description,location)
    )

    conn.commit()
    conn.close()

    return jsonify({"status":"success"})


@app.route("/issues",methods=["GET"])
def get_issues():

    conn=get_db()
    cur=conn.cursor()

    cur.execute("SELECT * FROM issues")

    rows=cur.fetchall()

    issues=[dict(row) for row in rows]

    conn.close()

    return jsonify(issues)


if __name__=="__main__":
    app.run(debug=True)
