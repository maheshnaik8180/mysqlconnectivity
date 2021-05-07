import os
import sys
import mysql.connector as mysql
import logging
from dotenv import *

from log import logger

# Function to Connect to the database
# def mysqlconnect():
#     try:
#         mysqldb = mysql.connector.connect(host="localhost", user="root", password="admin",
#                                           database="payroll_service")
#         logger.info("Database Successfully Connected")
#     except Exception:
#         logger.error("Can't Connect")
#     else:
#         return mysqldb

load_dotenv(find_dotenv())
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB')


class mysqlconn:
    def __init__(self, db_host, db_user, db_pass, db_name):
        self.mydb = mysql.connector.connect(host= db_host, user= db_user, password= db_pass, database= db_name)
        self.mycursor = self.mydb.cursor()

    # Function to close database connection
    def close_conn(self):
        self.mydb.close()

    # Function to Display Table
    def display(self):
        mysqldb = self.mycursor
        mycursor = mysqldb.cursor()
        sql_query = "SELECT * FROM employee_payroll"
        try:
            mycursor.execute(sql_query)
            result = mycursor.fetchall()
            for i in result:
                emp_id = i[0]
                name = i[1]
                gender = i[2]
                salary = i[3]
                start = i[4]

                logger.info(f"id:{emp_id},name:{name},gender:{gender},salary:{salary},start:{start}")
        except Exception:
            logger.error('Error:Unable to fetch data.')
        mysqldb.close()

    # Function to Update Data
    def updatadata(self):
        mysqldb = self.mycursor
        mycursor = mysqldb.cursor()
        sql_query1 = "UPDATE employee_payroll SET salary=30000 WHERE name='bill'"
        sql_query2 = "SELECT * FROM employee_payroll WHERE name='James'"
        try:
            mycursor.execute(sql_query1)
            mysqldb.commit()
            logger.info('Record Updated successfully')
        except Exception:
            logger.error("Error! unable to update data")
            mysqldb.rollback()
        mysqldb.close()

    # Function to Delete Data
    def deletedata(self):
        mysqldb = self.mycursor
        mycursor = mysqldb.cursor()
        sql_query = "DELETE FROM employee_payroll WHERE name='chalie'"
        try:
            mycursor.execute(sql_query)
            mysqldb.commit()
            logger.info('Record Deteted Successfully')
        except Exception:
            logger.error("Error! unable to update data")
            mysqldb.rollback()
        mysqldb.close()


# Driver Function
if __name__ == "__main__":
    dbconn = mysqlconn(db_host, db_user, db_pass, db_name)
    logger.setLevel(logging.INFO)
    dbconn.display()
    dbconn.updatadata()
    dbconn.deletedata()
