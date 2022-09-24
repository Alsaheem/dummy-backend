import flask
from flask import Flask

app = Flask(__name__)

version = "v1"

@app.route("/status")
def status():
    response = flask.jsonify({"success": True})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200


@app.route("/posts")
def posts():
    posts = [
        {
            "name": "hoodie 101",
            "url": "https://images.unsplash.com/photo-1590316519564-ebeeca222a95?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG9vZGllfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
        },
        {
            "name": "hoodie 102",
            "url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8aG9vZGllfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
        },
        {
            "name": "hoodie 103",
            "url": "https://images.unsplash.com/photo-1513789181297-6f2ec112c0bc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8aG9vZGllfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
        },
        {
            "name": "hoodie 104",
            "url": "https://images.unsplash.com/photo-1579572331145-5e53b299c64e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aG9vZGllfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60",
        },
    ]
    response = flask.jsonify({"posts": posts, "version": "v1"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 200

    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)        