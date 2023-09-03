import pymysql
import re
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
    if None in [userid, pw, tel, sex, age] :
        return '값을 입력하세요.'
    else :
        if sex == 'w' or sex == 'm' :
            if re.compile("^(01)\d{1}-\d{3,4}-\d{4}$").search(tel.replace(" ", "")) : 
                cur = conn.cursor()
                sql = f"insert into `mask`.`members` values (null, '{userid}', '{pw}', {tel}, '{sex}', {age});"
                
                cur.execute(sql)
                
                return 'completion'
            else : return '전화번호 입력 형식은 [01X-XXX(X)-XXXX]입니다. 확인하세요.'
        else : return '성별은 여성(w)과 남성(m)만 선택할 수 있습니다.'

def putChangeContent(id, mainAgent, changed) :
    cur = conn.cursor()
    f = False
    if None in [id, mainAgent, changed] :
        return '값을 입력하세요.'
    else :
        if mainAgent == 'age' : sql = f"update `mask`.`members` set `{mainAgent}` = {int(changed)} where `id` = {id};"
        else:
            if bool(changed == ['w', 'm'] and mainAgent == 'sex') or bool(re.compile("^(01)\d{1}-\d{3,4}-\d{4}$").search(changed.replace(" ", "")) and mainAgent == 'tel') or mainAgent in ['userid, pw']:
                f = True

        if f :
            sql = f"update `mask`.`members` set `{mainAgent}` = '{changed}' where `id` = {id};"
            cur.execute(sql)
    
            return 'completion'

def Delete(userid) :
    cur = conn.cursor()
    sql = f"delete from `mask`.`members` where id = '{userid}';"
    
    cur.execute(sql)
    
    return 'completion'