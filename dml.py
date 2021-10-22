from typing import FrozenSet
import mysql.connector as myq


def check_courier(id):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    i = tuple([id])
    mycur.callproc('c_exist', i)
    for result in mycur.stored_results():
        res = result.fetchall()
        for row in res:
            val = row[0]
    mycur.close()
    mydb.close()
    if val == 1:
        return 1
    else:
        return 0


def updt_courier(id, og, ds, dt, t):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    arg = (id, og, ds, dt, t)
    try:
        mycur.callproc('updt_c_det', arg)
        mydb.commit()
        mycur.close()
        mydb.close()
        return 1
    except:
        return 0


def staff_det(nm, pw, ph):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    sql = "INSERT INTO staff (name,pw,ph) VALUES (%s,%s,%s)"
    val = (str(nm), str(pw), str(ph))
    try:
        mycur.execute(sql, val)
        mycur.execute("SELECT LAST_INSERT_ID()")
        res = mycur.fetchall()
        for x in res:
            id = x[0]
        print(id)
        mydb.commit()
        mycur.close()
        mydb.close()
        return id
    except:
        return 0


def insert_data_c_details(org, dest):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    sql = "INSERT INTO c_details (origin,dest) VALUES (%s,%s)"
    val = (str(org), str(dest))
    mycur.execute(sql, val)
    mycur.execute("SELECT LAST_INSERT_ID()")
    res = mycur.fetchall()
    for x in res:
        id = x[0]
    mydb.commit()
    mycur.close()
    mydb.close()
    print(mycur.rowcount, "Record Inserted")
    return id


def insert_data_c_og(id, d_reg, typ):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    sql = "INSERT INTO c_sched_og VALUES (%s,%s,%s)"
    val = (str(id), str(d_reg), str(typ))
    mycur.execute(sql, val)
    mydb.commit()
    mycur.close()
    mydb.close()
    print(mycur.rowcount, "Record Inserted")


def insert_data_c_staff(id, nm, ph):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    sql = "INSERT INTO c_staff VALUES (%s,%s,%s)"
    val = (str(id), str(nm), str(ph))
    mycur.execute(sql, val)
    mydb.commit()
    mycur.close()
    mydb.close()
    print(mycur.rowcount, "Record Inserted")


def insert_data_c_receiver(id, nm, ph):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    sql = "INSERT INTO rec_det VALUES (%s,%s,%s)"
    val = (str(id), str(nm), str(ph))
    mycur.execute(sql, val)
    mydb.commit()
    mycur.close()
    mydb.close()
    print(mycur.rowcount, "Record Inserted")


def user_det(nm, id, pw):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    sql = "INSERT INTO user_det VALUES (%s,%s,%s)"
    val = (str(id), str(pw), str(nm))
    try:
        mycur.execute(sql, val)
        mydb.commit()
        mycur.close()
        mydb.close()
        return 1
    except:
        return 0


def del_data(id):
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("USE COURIER")
    arg = tuple([id])
    try:
        mycur.callproc('del_id', arg)
        mydb.commit()
        mycur.close()
        mydb.close()
        return 1
    except:
        return 0

