import os
import mysql.connector
from dotenv import *
import logging

# logger implementation
from log import logger

load_dotenv(find_dotenv())

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB')


class DBconnection:
    logger.setLevel(logging.INFO)
    # Constructor for Server class
    def __init__(self, db_host, db_user, db_pass, db_name):
        self.conn = mysql.connector.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
        self.cursor = self.conn.cursor()

        # Function to close database connection

    def close_conn(self):
        self.conn.close()

    def display(self):
        sql_query = "SELECT * FROM employee_payroll;"
        try:
            self.cursor.execute(sql_query)
            result = self.cursor.fetchall()
            for i in result:
                emp_id = i[0]
                name = i[1]
                gender = i[2]
                salary = i[3]
                start = i[4]
                logger.info(f"id:{emp_id},name:{name},gender:{gender},salary:{salary},start:{start}")
        except Exception:
                logger.error('Error:Unable to fetch data.')

    def InsertRecord(self):
        query = "INSERT INTO employee_payroll(id, name, gender, salary, start) VALUES(6, 'vikas', 'M', 400000, '2018-06-05');"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            logger.info('Record Inserted Successfully')
        except Exception:
            logger.error("Error! unable to insert data")
            self.conn.rollback()

    def updatadata(self):
        query1 = "UPDATE employee_payroll SET salary=30000 WHERE name='bill'"
        query2 = "SELECT * FROM employee_payroll WHERE name='James'"
        try:
            self.cursor.execute(query1)
            self.conn.commit()
            logger.info('Record Updated successfully')
        except Exception:
            logger.info("Error! unable to update data")
            self.conn.rollback()

    def deletedata(self):

        query = "DELETE FROM employee_payroll WHERE name='chalie'"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            logger.info('Record Deteted Successfully')
        except Exception:
            logger.error("Error! unable to update data")
            self.conn.rollback()


# Drivers Function
dbconn = DBconnection(db_host, db_user, db_pass, db_name)
dbconn.display()
dbconn.InsertRecord()
dbconn.updatadata()
dbconn.deletedata()

