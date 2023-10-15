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

    sql = f"select * from members where `id` = {Id}"
    cur.execute(sql)
    cur = tuple(cur)

    result = {}
    result["id"] = cur[0][0]
    result["userId"] = cur[0][1]
    result["password"] = cur[0][2]
    result["tel"] = cur[0][3]
    result["sex"] = cur[0][4]
    result["age"] = cur[0][5]
    
    return result

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

def putChangeContent(id, request) :
    # 기본적으로 update를 모든 필드를 바꾸게끔 (id만 빼고)
    # id로 유저를 조회

    cur = conn.cursor()

    sql = f"select * from members where `id` = {id}"
    cur.execute(sql)
    cur = tuple(cur)

    base = {
        "userId": cur[0][1],
        "pw":cur[0][2],
        "tel":cur[0][3],
        "sex":cur[0][4],
        "age":cur[0][5]
    }  

    for key, value in request.items():
        if key in base : 
            base[key] = value


    cur = conn.cursor()
    sql = f"update `mask`.`members` set `userId` = '{base['userId']}', `pw` = '{base['pw']}', `tel` = '{base['tel']}', `sex` = '{base['sex']}', `age` = {base['age']} where `id` = {id};"
    cur.execute(sql)
    
    return 'completion'

def Delete(userid) :
    cur = conn.cursor()
    sql = f"delete from `mask`.`members` where id = '{userid}';"
    
    cur.execute(sql)
    
    return 'completion'