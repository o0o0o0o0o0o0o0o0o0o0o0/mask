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

@app.route("/users/by-condition/<int:id>" , methods=["GET"])
def usersByCondition(id):
    p = gui.getIdPassByCondition(id)
    message = {
        "result":p
    }
    return message

@app.route("/users/signup" , methods=["POST"])
def usersSignup():

    request_body = request.get_json()
    userid = request_body["id"]
    pw = request_body["pw"]
    tel = request_body["tel"]
    sex = request_body["sex"]
    age = request_body["age"]

    p = gui.postMemberSignUp(userid, pw, tel, sex, age)
    message = {
        "result":p
    }
    return message

@app.route("/users/change/<int:id>" , methods=["PUT"])
def usersChange(id):
    requestBody = request.get_json()
    mainAgent = requestBody["mainAgent"]
    changed = requestBody["changed"]

    p = gui.putChangeContent(id, mainAgent, changed)
    message = {
        "result":p
    }
    return message

@app.route("/users/delete/<int:id>" , methods=["Delete"])
def usersDelete(id):
    
    p = gui.Delete(id)
    message = {
        "result":p
    }
    return message

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
