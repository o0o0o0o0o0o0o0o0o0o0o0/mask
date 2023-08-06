import pymysql
conn = pymysql.connect(host = "localhost", db = "mask", user ="root", password = "jennyyoon0814")

cur = conn.cursor()

def login(id, password) :
    f = True
    command = "select * from members where id = %s"
    cur.execute(command, (id))
    for i in cur :
        if password == i[1] :
            print('로그인 완료')
            f = False
    if f :
        print('로그인 실패: 아이디 또는 패스워드가 잘못되었습니다.')


def join (id, pw) :
    f = True
    compareCommand = "select * from memberInformations where id = %s"
    cur.execute(compareCommand, (id))
    for i in cur :
        f = False
        print('아이디가 중복 됩니다')
    if f: 
        insertCommand = "insert into `mask`.`memberInformations` values(%s, %s);"
        cur.execute(insertCommand, (id, pw))
        conn.commit()
    
def joinS(n, l, ex, id, pw) :
    join(id, pw)
    insertCommand = "insert into `mask`.`insm` values(%s, %s, %s, %s);"
    cur.execute(insertCommand, (n, l, ex, id))
    conn.commit()
    print('회원가입 완료')

def joinD(id, pw) :
    join(id, pw)
    insertCommand = "insert into `mask`.`insm` values(%s);"
    cur.execute(insertCommand, (id))
    conn.commit()
    print('회원가입 완료')


if __name__=="__main__":
    id, pw = input().split()
    joinD(id, pw)

    id, pw = input().split()
    name, loc, ex = input().split()
    joinS(name, loc, ex, id, pw)

conn.close()
# fechall
# fetchone