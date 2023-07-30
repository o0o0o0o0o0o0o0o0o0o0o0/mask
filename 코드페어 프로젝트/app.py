from flask import Flask, request
import getUserInfo

app = Flask(__name__)
@app.route("/users" , methods=["GET"])
def users():
    p = getUserInfo.getIdPass()
    message = {
        "result":p
    }
    return message

@app.route("/users/by-condition" , methods=["GET"])
def usersByCondition():
    p = getUserInfo.getIdPassByCondition(request.args.get("id"))
    print(p)
    message = {
        "result":p
    }
    return message


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

    #문자 일부만 검색해도 나오게 하기