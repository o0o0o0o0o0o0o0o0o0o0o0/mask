from flask import Flask, request
import getUserInfo as gui
import bulletinInfo as bi

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

#-----------------------------------------------------------------------------------------------------------------------------

@app.route("/bulletin/by-condition/all", methods=["GET"])
def bulletinByConditionA() :
    p = bi.getInfoByConditionA()

    message = {
        "result":p
    }
    return message

@app.route("/bulletin/by-condition/<string:category>/<string:search>", methods=["GET"])
def bulletinByCondition(search, category) :
    p = bi.getInfoByCondition(search, category)

    message = {
        "result":p
    }
    return message

@app.route("/bulletin/add-bulletin/", methods=["POST"])
def AddBulletin() :
    request_body = request.get_json()
    userId = request_body["userId"]
    title = request_body["title"]
    deliveryDueDate = request_body["deliveryDueDate"]
    contents = request_body["contents"]

    p = bi.postAddBulletin(userId, title, deliveryDueDate, contents)
    message = {
        "result":p
    }
    return message

@app.route("/bulletin/change/<int:id>" , methods=["PUT"])
def bulletinChange(id):
    requestBody = request.get_json()
    mainAgent = requestBody["mainAgent"]
    changed = requestBody["changed"]

    p = bi.putChangeContent(id, mainAgent, changed)
    message = {
        "result":p
    }
    return message

@app.route("/bulletin/delete/<int:id>" , methods=["DELETE"])
def bulletinDelete(id):

    p = bi.Delete(id)
    message = {
        "result":p
    }
    return message

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)