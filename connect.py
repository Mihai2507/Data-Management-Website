import time

import pymysql.cursors


class DBConnection:
    connection = None

    def __init__(self):
        self.get_connection()

    def get_connection(self):
        if self.connection is None:
            self.connection = self.__connect_to_mysql()
        return self.connection

    def __connect_to_mysql(self):  # noqa
        retries = 0
        max_retries = 10
        while retries < max_retries:
            try:
                db_connection = pymysql.connect(host="127.0.0.1",
                                                port=3306,
                                                user='root',
                                                # password='flaskpassword',
                                                database='cursanti',
                                                cursorclass=pymysql.cursors.DictCursor)
                if db_connection:
                    print('Connection established')
                    return db_connection
            except Exception as e:
                print(f"Failed to connect to MySQL (Attempt {retries + 1}/{max_retries}): {e}")
                retries += 1
                time.sleep(15)
        raise Exception("Failed to connect to MySQL after multiple retries")