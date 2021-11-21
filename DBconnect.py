import sys
import pymysql
from PyQt5.QtWidgets import QMessageBox


def main_menu():

    print("select feaeture ")
    print("1: view every user")
    print("2: insert user")
    print("3: search user by id , pwd")
    print("4: sql command ")
    print("other: exit")
    menu = int(input("select : "))

    if menu == 1:
        view_every_user()
    elif menu == 2:
        insert_user()
    elif menu == 3:
        search_user()
    elif menu == 4:
        SqlCall()
    elif menu == 5:
        id = int(input("id: "))
        pwd = str(input("pwd: "))
        LoginCheck(id,pwd)

    else:
        sys.exit()



#Sql문을 바로 질의 할 수 있는 함수 필요시 사용
def SqlCall():

    while(1):
        conn = pymysql.connect(
            host='database2021db.cxk1zwfumcmo.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='test!234',
            db='teamprj',
            charset='utf8'
        )
        conn.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        sql = input("sql : ")

        try:
            if sql == "exit":
                return

            cursor.execute(sql) #sql문 실행
            result = cursor.fetchall() #결과물 fetch

            print(result)


            if result == ():
                print("there is no match data")

            if len(result) > 1:
                print("there are more then one response")





        finally:
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

    result = -1
    try:
        cursor.execute(sql)
        conn.commit() #DB 변경내용 저장
        result = cursor.fetchall()

    finally:
        conn.close()  #DB 연결종료
        return result; #성공시 결과값 반환, 실패시 -1 반환

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


#login check
def LoginCheck(id,pwd):

    sql_q = "select * from user where user_id = " + str(id) + " and pwd = '" + str(pwd) + "'; "
    print("실행된 sql 쿼리: "+sql_q)

    try:
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
        if result != () :
            #결과가 널이 아님
            #로그인 성공
            return 1
        else:
            #결과가 널값
            #로그인 실패
            return 0

    finally:
        conn.close()  # DB 연결종료


#아이디 중복체크 함수
def IdDuplicateCheck(id):
    try:
        conn = pymysql.connect(
            host='database2021db.cxk1zwfumcmo.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='test!234',
            db='teamprj',
            charset='utf8'
        )
        conn.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql_q = "select * from user where user_id =" + str(id) + ";"
        print(sql_q)
        cursor.execute(sql_q)

        result = cursor.fetchall()
        if result == ():
            #중복이 없을 경우 팝업을 띄우고 1을 반환
            print("there is no dupilicate")
            show_popup_ok("no dupilicate","you can use this id")
            return 1
        else:
            #중복이 생길경우 팝업을 띄우고 0을 반환
            print("there is already exist same id in data")
            show_popup_ok("dupilicate", "you can't use this id, \n there is already exist")
            return 0
    finally:
        conn.close()


def show_popup_ok(title: str, content: str):

    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(content)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

if __name__ == "__main__":
    while(1):
        main_menu()



# insert into user values('99','test_pwd','test_name','male','1999-10-20','010-1234-5678','2021-11-12');




