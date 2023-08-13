import pymysql
conn = pymysql.connect(host = "localhost", db = "mask", user ="root", password = "jennyyoon0814")

def getIdPass():

    cur = conn.cursor()

    sql = "select * from memberInformations"

    cur.execute(sql)

    total = []
    
    for i in cur:
        result = {}
        result["id"] = i[0]
        result["password"] = i[1]
        result["tel"] = i[2]
        result["sex"] = i[3]
        result["age"] = i[4]

        total.append(result)
    
    return total

def getIdPassByCondition(Id):

    cur = conn.cursor()

    sql = "select * from memberInformations where `id` like '%" + Id + "%'"
    cur.execute(sql)

    total = []
    
    for i in cur:
        result = {}
        result["id"] = i[0]
        result["password"] = i[1]
        result["tel"] = i[2]
        result["sex"] = i[3]
        result["age"] = i[4]

        total.append(result)
    
    return total

def postMemberSignUp(id, pw, tel, sex, age) :
    cur = conn.cursor()
    sql = f"insert into `mask`.`memberInformations`values ('{id}', '{pw}', {tel}, '{sex}', {age});"
    print(sql)
    cur.execute(sql)
    
    return 'completion'

def putChangeContent(id, mainAgent, changed) :
    cur = conn.cursor()
    if mainAgent == 'age' or mainAgent == 'tel' : sql = f"update `mask`.`memberInformations` set `{mainAgent}` = {changed} where `id` = '{id}';"
    else: sql = f"update `mask`.`memberInformations` set `{mainAgent}` = '{changed}' where `id` = '{id}';"
    print(sql)
    cur.execute(sql)
    
    return 'completion'

def Delete(id) :
    cur = conn.cursor()
    sql = f"delete from `mask`.`memberInformations` where id = '{id}';"
    print(sql)
    cur.execute(sql)
    
    return 'completion'