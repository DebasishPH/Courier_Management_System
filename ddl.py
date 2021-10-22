import mysql.connector as myq


def create_data():
    mydb = myq.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycur = mydb.cursor()
    mycur.execute("CREATE DATABASE IF NOT EXISTS courier")
    mycur.execute("USE COURIER")
    mycur.execute(
        "CREATE TABLE IF NOT EXISTS c_details (ID INT NOT NULL AUTO_INCREMENT,origin VARCHAR(20),dest VARCHAR(20), PRIMARY KEY(ID))")
    mycur.execute(
        "CREATE TABLE IF NOT EXISTS c_sched_og (ID INT NOT NULL UNIQUE,d_of_reg DATE,type VARCHAR(20),FOREIGN KEY(ID) REFERENCES c_details(ID) ON DELETE CASCADE)")
    mycur.execute(
        "CREATE TABLE IF NOT EXISTS c_sched_dest (ID INT NOT NULL UNIQUE,d_of_del DATE,FOREIGN KEY(ID) REFERENCES c_details(ID) ON DELETE CASCADE)")
    mycur.execute(
        "CREATE TABLE IF NOT EXISTS staff (s_id INT NOT NULL AUTO_INCREMENT,name VARCHAR(20), pw VARCHAR(20),ph INT NOT NULL UNIQUE,PRIMARY KEY(s_id))")
    mycur.execute("CREATE TABLE IF NOT EXISTS rec_det (r_id INT NOT NULL,name VARCHAR(20) NOT NULL,phone int NOT NULL UNIQUE, FOREIGN KEY(r_id) REFERENCES c_details(ID) ON DELETE CASCADE)")
    mycur.execute(
        "CREATE TABLE IF NOT EXISTS user_det (u_id VARCHAR(20) NOT NULL UNIQUE,pw VARCHAR(20),name VARCHAR(20))")
    mydb.commit()
    mycur.close()
    mydb.close()
