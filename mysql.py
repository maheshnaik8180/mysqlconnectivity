import mysql.connector
import os
from decouple import config
class mysql:
    def __init__(self):
        self.mydb = mysql.connect(host=config('localhost'), user=config('root'), password=config('admin'),
                                  database=config('database'))
        self.mycursor = self.mydb.cursor()
    # Function to Connect to the database
    # def mysqlconnect(self):
    #     try:
    #         mysqldb = mysql.connector.connect(host="localhost", user="root", password="admin",
    #                                       database="payroll_service")
    #         print("Database Successfully Connected")
    #     except Exception:
    #         print("Can't Connect")
    #     else:
    #         return mysqldb


    # Function to Display Table
    def display(self):
        mysqldb = mysqlconnect()
        mycursor = mysqldb.cursor()
        sql_query = "SELECT * FROM employee_payroll"
        try:
            mycursor.execute(sql_query)
            result = mycursor.fetchall()
            for i in result:
                id = i[0]
                name = i[1]
                gender = i[2]
                salary = i[3]
                start = i[4]

                print(f"id:{id},name:{name},gender:{gender},salary:{salary},start:{start}")
        except Exception:
         print('Error:Unable to fetch data.')
         mysqldb.close()




# Driver Function
if __name__ == "__main__":
    logger.setLevel(logging.INFO)
    display()
