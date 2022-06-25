
from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200

# Get Method
DATA = {
    "Employee": {
        "Rohit":"Developer",
        "Pratik":"Tester",
        "Jack":"Manager",
        "Milind":"Devops",
        "Priyanka":"Fromtend",
    },
    "Locations":{
        "Afourtech":"Pune",
        "Opstree":"Delhi",
        "Cloudera":"Banglore",
        "Mindtree":"Mumbai",
        "Spacetech":"Chennai",
    },
    "CICD":{
        "AWS":"Codepipeline",
        "Azure":"Azure Devops",
        "OpenSource":"Jenkins",
        "IBM":"Udeploy",
    }
}

@app.route("/")
def home():
   return "<h1 style='color:green'>This is root!</h1>"

@app.route('/home')
def hello_world():
    return render_template('index.html')

@app.route("/qstr")
def qs():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res

    res = make_response(jsonify({"error": "No Query String"}), 404)
    return res

@app.route("/json")
def get_json():
    res = make_response(jsonify(DATA), 200)
    return res

@app.route("/json/<collection>/<member>")
def get_data(collection, member):
    print("getting the value of %s in the collection %s"%(member,collection))
    if collection in DATA:
        member = DATA[collection].get(member)
        if member:
            res = make_response(jsonify({"res":member}), 200)
            return res

        res = make_response(jsonify({"error": "Not found"}), 404)
        return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res

# Post Method

@app.route("/json/<collection>", methods=["POST"])
def create_col(collection):

    req = request.get_json()

    if collection in DATA:
        res = make_response(jsonify({"error": "Collection already exists"}), 400)
        return res

    DATA.update({collection: req})

    res = make_response(jsonify({"message": "Collection created"}), 201)
    return res

# Put Method

@app.route("/json/<collection>/<member>", methods=["PUT"])
def put_col_mem(collection,member):

    req = request.get_json()

    if collection in DATA:
        if member:
            print(req)
            DATA[collection][member] = req["new"]
            res = make_response(jsonify({"res":DATA[collection]}), 200)
            return res

        res = make_response(jsonify({"error": "Not found"}), 404)
        return res

    res = make_response(jsonify({"error": "Not found"}), 404)
    return res

# Delete Method

@app.route("/json/<collection>", methods=["DELETE"])
def delete_col(collection):

    if collection in DATA:
        del DATA[collection]
        res = make_response(jsonify(DATA), 200)
        return res

    res = make_response(jsonify({"error": "Collection not found"}), 404)
    return res

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host='0.0.0.0', port=PORT)
