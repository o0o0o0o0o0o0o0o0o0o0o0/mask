import pymysql
conn = pymysql.connect(host = "localhost", db = "mask", user ="root", password = "jennyyoon0814")

def getIdPass():

    cur = conn.cursor()

    sql = "select * from members"

    cur.execute(sql)

    total = []
    
    for i in cur.fetchall():
        result = {}
        result["id"] = i[0]
        result["userId"] = i[1]
        result["password"] = i[2]
        result["tel"] = i[3]
        result["sex"] = i[4]
        result["age"] = i[5]

        total.append(result)
    
    return total

def getIdPassByCondition(Id):

    cur = conn.cursor()

    sql = "select * from members where `id` like '%" + Id + "%'"
    cur.execute(sql)

    total = []
    
    for i in cur:
        result = {}
        result["id"] = i[0]
        result["userId"] = i[1]
        result["password"] = i[2]
        result["tel"] = i[3]
        result["sex"] = i[4]
        result["age"] = i[5]

        total.append(result)
    
    return total

def postMemberSignUp(userid, pw, tel, sex, age) :
    cur = conn.cursor()
    sql = f"insert into `mask`.`members` values (null, '{userid}', '{pw}', {tel}, '{sex}', {age});"
    
    cur.execute(sql)
    
    return 'completion'

def putChangeContent(id, mainAgent, changed) :
    cur = conn.cursor()
    if mainAgent == 'age' or mainAgent == 'tel' : sql = f"update `mask`.`members` set `{mainAgent}` = {int(changed)} where `id` = {id};"
    else: sql = f"update `mask`.`members` set `{mainAgent}` = '{changed}' where `id` = {id};"
    
    cur.execute(sql)
    
    return 'completion'

def Delete(userid) :
    cur = conn.cursor()
    sql = f"delete from `mask`.`members` where id = '{userid}';"
    
    cur.execute(sql)
    
    return 'completion'