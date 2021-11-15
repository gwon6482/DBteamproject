import sys
import pymysql

#Sql문을 바로 질의 할 수 있는 함수 필요시 사용
def SqlCall():
    conn = pymysql.connect(
        host='database2021db.cxk1zwfumcmo.ap-northeast-2.rds.amazonaws.com',
        user='admin',
        password='test!234',
        db='teamprj',
        charset='utf8'
    )
    conn.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    while(1):
        sql = input("sql : ")

        if sql == "exit":
            break

        cursor.execute(sql) #sql문 실행
        result = cursor.fetchall() #결과물 fetch

        for i in result:
            print(i)

        conn.commit()
        conn.close()  # DB 연결종료



#매개변수로 Sql 쿼리문을 String형태로 받아 바로 실행 및 결과 저장
#접속 -> 쿼리 실행 -> 저장 -> 접속 종료의 순서 로 실행
def SqlCommand(sql):
    conn = pymysql.connect(
        host='database2021db.cxk1zwfumcmo.ap-northeast-2.rds.amazonaws.com',
        user='admin',
        password='test!234',
        db='teamprj',
        charset='utf8'
    )
    conn.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql)
    conn.commit() #DB 변경내용 저장
    conn.close()  #DB 연결종료


def main_menu():

    print("select feaeture ")
    print("1: view every user")
    print("2: insert user")
    print("3: search user by id , pwd")
    print("other: exit")
    menu = int(input("select : "))

    if menu == 1:
        view_every_user()
    elif menu == 2:
        insert_user()
    elif menu == 3:
        search_user()
    else:
        sys.exit()





def view_every_user():
    print("start")

    conn = pymysql.connect(
        host='database2021db.cxk1zwfumcmo.ap-northeast-2.rds.amazonaws.com',
        user='admin',
        password='test!234',
        db='teamprj',
        charset='utf8'
    )
    conn.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql_q = "select * from user"
    cursor.execute(sql_q)

    result = cursor.fetchall()  # 결과물 fetch
    for i in result:
        print(i)
    print()

    conn.commit()  # DB 변경내용 저장
    conn.close()  # DB 연결종료


def insert_user():
    id = str(input("id: "))
    pwd = str(input("pwd: "))
    name = str(input("name: "))
    sex = str(input("sex: "))
    brth = str(input("brth: "))
    phone = str(input("phone: "))
    r_date = str(input("r_date: "))

    sql_q = "insert into user values('" + id + "', '" + pwd + "', '" + name + "', '" + sex + "', '" + brth + "', '" + phone + "' , '" + r_date + "');"
    conn = pymysql.connect(
        host='database2021db.cxk1zwfumcmo.ap-northeast-2.rds.amazonaws.com',
        user='admin',
        password='test!234',
        db='teamprj',
        charset='utf8'
    )
    conn.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_q)
    conn.commit()  # DB 변경내용 저장
    conn.close()  # DB 연결종료


def search_user():
    s_id = str(input("id: "))
    s_pwd = str(input("pwd: "))
    sql_q = "select * from user where user_id = '" + s_id + "' AND pwd = '" + s_pwd +"' ;"
    conn = pymysql.connect(
        host='database2021db.cxk1zwfumcmo.ap-northeast-2.rds.amazonaws.com',
        user='admin',
        password='test!234',
        db='teamprj',
        charset='utf8'
    )
    conn.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql_q)
    result = cursor.fetchall()
    print(result)
    conn.commit()  # DB 변경내용 저장
    conn.close()  # DB 연결종료

if __name__ == "__main__":
    while(1):
        main_menu()



# insert into user values('99','test_pwd','test_name','male','1999-10-20','010-1234-5678','2021-11-12');