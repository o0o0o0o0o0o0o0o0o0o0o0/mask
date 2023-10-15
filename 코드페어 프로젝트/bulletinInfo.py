import pymysql
conn = pymysql.connect(host = "localhost", db = "mask", user ="root", password = "jennyyoon0814")
import datetime

def getInfoByConditionA():

    cur = conn.cursor()

    sql = "select * from bulletin"
    cur.execute(sql)

    total = []
    
    for i in cur:
        result = {}
        result["id"] = i[0]
        result["userId"] = i[1]
        result["title"] = i[2]
        result["createdAt"] = i[3]
        result["updatedAt"] = i[4]
        result["deliveryDueDate"] = i[5]
        result["contents"] = i[6]

        total.append(result)
    
    return total

def getInfoByCondition(search, category):

    cur = conn.cursor()

    sql = "select * from bulletin where `" + category + "` like '%" + search + "%'"
    cur.execute(sql)

    total = []
    
    for i in cur:
        result = {}
        result["id"] = i[0]
        result["userId"] = i[1]
        result["title"] = i[2]
        result["createdAt"] = i[3]
        result["updatedAt"] = i[4]
        result["deliveryDueDate"] = i[5]
        result["contents"] = i[6]

        total.append(result)
    
    return total

def postAddBulletin(userid, title, deliveryDueDate, contents) :
    now = datetime.datetime.now().strftime('%Y-%m-%d')

    cur = conn.cursor()
    sql = f"insert into `mask`.`bulletin` values (null, {userid}, '{title}', '{now}', '{now}', '{deliveryDueDate}', '{contents}');"
    
    cur.execute(sql)
    
    return 'completion'

def putChangeContent(id, request) :
    # 기본적으로 update를 모든 필드를 바꾸게끔 (id만 빼고)
    # id로 유저를 조회

    cur = conn.cursor()

    sql = f"select * from bulletin where `id` = {id}"
    cur.execute(sql)
    cur = tuple(cur)

    base = {
        "title":cur[0][2],
        "updatedAt":cur[0][4],
        "deliveryDueDate":cur[0][5],
        "contents":cur[0][6],
    }  

    for key, value in request.items():
        if key in base and bool(key != 'updatedAt' or key != 'createdAt'): 
            base[key] = value

    # userid, title, deliveryDueDate, contents
    cur = conn.cursor()
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    sql = f"update `mask`.`bulletin` set `title` = '{base['title']}', `updatedAt` = '{now}', `deliveryDueDate` = '{base['deliveryDueDate']}', `contents` = '{base['contents']}' where `id` = {id};"
    cur.execute(sql)
    
    return 'completion'

def Delete(id) :
    cur = conn.cursor()
    sql = f"delete from `mask`.`bulletin` where id = '{id}';"
    
    cur.execute(sql)
    
    return 'completion'