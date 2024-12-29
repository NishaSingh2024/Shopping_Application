import mysql.connector
from mysql.connector import Error


class MYSQL_CONNECTION:
    cursor=''
    
    @classmethod
    def ExecuteQuery(cls,query):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='myntra',
                                                user='root',
                                                password='python4u')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                # print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()

                return cursor.rowcount


                # record = MYSQL_CONNECTION.cursor.fetchone()
                # print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
            return 0

        finally:
            MYSQL_CONNECTION.CloseConnection(connection,cursor)
            
    
    @classmethod
    def CloseConnection(cls,connection,cursor):
        if connection.is_connected():
                cursor.close()
                connection.close()
                # print("MySQL connection is closed")



    @classmethod
    def getData(cls,query):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='myntra',
                                                user='root',
                                                password='python4u')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                # print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(query)
                return cursor.fetchall()


                # record = MYSQL_CONNECTION.cursor.fetchone()
                # print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
            return []

        finally:
              MYSQL_CONNECTION.CloseConnection(connection,cursor)
                