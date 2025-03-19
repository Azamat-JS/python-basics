from flask import Flask, jsonify, escape
import requests
app = Flask(__name__)
# flask --app app --debug run
@app.route('/')
def index():
    return {"message": "Salom Web"}

@app.route('/get')
def json():
    return jsonify(message="this is the first")

@app.route('/res', methods=["GET"])
def res():
    return jsonify(dict(status="OK")), 200

@app.route('/tez', methods=["GET", "POST"])
def tez():
    if request.method == "GET": return jsonify(status="OK", method="GET"), 200
    if request.method == "POST": return jsonify(status="OK", method="POST"), 200

@app.route('/query')
def query():
    course = request.args["course"]
    rating = request.args.get("rating")
    return {"message": f"{course} with rating {rating}"}

@app.route('/fetch')
def get_author():
    res = requests.get("https://url...")
    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message": "Something went wrong"}, 404
    else:
        return {"message": "server error"}, 500
    

# ----- dynamic url
@app.route('/fetch/<isbn>')
def get_author(isbn):
    res = requests.get("https://url.org/isbn/{escape(isbn)}.JSON")
    if res.status_code == 200:
        return {"message": res.JSON()}
    elif res.status_code == 404:
        return {"message": "Something went wrong"}, 404
    else:
        return {"message": "server error"}, 500
    
# @app.route("termianls/<string:airport_code>")
# @app.route('/book/<int:isbn>')