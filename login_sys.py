import mysql.connector as myq


def check_login(id, pw):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    arg = tuple([id])
    mycur.callproc('disp_det', arg)
    for result in mycur.stored_results():
        res = result.fetchall()
    if len(res) != 0:
        for row in res:
            ret_pw = row[0]
            ret_name = row[1]
        mycur.close()
        mydb.close()
        if str(ret_pw) == str(pw):
            return ret_name

    return "ERROR"


def check_login_emp(id, pw):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    arg = tuple([id])
    mycur.callproc('disp_emp', arg)
    for result in mycur.stored_results():
        res = result.fetchall()
    if len(res) != 0:
        for row in res:
            ret_pw = row[0]
            ret_name = row[1]
        mycur.close()
        mydb.close()
        if str(ret_pw) == str(pw):
            return ret_name
    return "ERROR"
