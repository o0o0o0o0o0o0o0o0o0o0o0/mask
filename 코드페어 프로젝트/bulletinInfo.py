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

def putChangeContent(id, mainAgent, changed) :
    now = datetime.datetime.now().strftime('%Y-%m-%d')

    cur = conn.cursor()
    if mainAgent == 'title' or mainAgent == 'contents' : sql = f"update `mask`.`bulletin` set `{mainAgent}` = '{changed}' where `id` = {id};"
    else: sql = f"update `mask`.`bulletin` set `{mainAgent}` = {int(changed)} where `id` = {id};"
    
    cur.execute(sql)
    sql = f"update `mask`.`bulletin` set `updatedAt` = '{now}' where `id` = {id};"
    cur.execute(sql)

    return 'completion'

def Delete(id) :
    cur = conn.cursor()
    sql = f"delete from `mask`.`bulletin` where id = '{id}';"
    
    cur.execute(sql)
    
    return 'completion'