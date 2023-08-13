from flask import Flask, request
import getUserInfo as gui

app = Flask(__name__)
@app.route("/users" , methods=["GET"])
def users():
    p = gui.getIdPass()
    message = {
        "result":p
    }
    return message

@app.route("/users/by-condition" , methods=["GET"])
def usersByCondition():
    p = gui.getIdPassByCondition(request.args.get("id"))
    print(p)
    message = {
        "result":p
    }
    return message

@app.route("/users/signup" , methods=["POST"])
def usersSignup():
    p = gui.postMemberSignUp(request.args.get("id"), request.args.get("pw"), request.args.get("tel"), request.args.get("sex"), request.args.get("age"))
    print(p)
    message = {
        "result":p
    }
    return message

@app.route("/users/change" , methods=["PUT"])
def usersChange():
    p = gui.postMemberSignUp(request.args.get("id"), request.args.get("mainAgent"), request.args.get("changed"))
    print(p)
    message = {
        "result":p
    }
    return message


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
