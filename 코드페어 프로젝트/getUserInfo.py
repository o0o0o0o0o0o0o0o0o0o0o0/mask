import pymysql
conn = pymysql.connect(host = "localhost", db = "mask", user ="root", password = "jennyyoon0814")

def getIdPass():

    cur = conn.cursor()

    sql = "select id, pw from memberInformations"

    cur.execute(sql)

    total = []
    
    for i in cur:
        result = {}
        result["id"] = i[0]
        result["password"] = i[1]

        total.append(result)
    
    return total

def getIdPassByCondition(Id):

    cur = conn.cursor()

    sql = "select id, pw from memberInformations where `id` like '%" + Id + "%'"
    cur.execute(sql)

    total = []
    
    for i in cur:
        result = {}
        result["id"] = i[0]
        result["password"] = i[1]

        total.append(result)
    
    return total

def postMemberSignUp(id, pw, tel, sex, age) :
    cur = conn.cursor()
    sql = "insert into `mask`.`memberInformations` values (" + id + ", " + pw, ", " + tel, ", " +  sex, ", " +  age + ");"
    cur.execute(sql)

    return