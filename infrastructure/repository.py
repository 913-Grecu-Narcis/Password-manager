from domain.user import User
import sqlite3

from infrastructure.repo_exception import RepoException


class Repository:
    def __init__(self, database='database.sqlite'):
        self.__database = database

    @property
    def database(self):
        return self.__database

    def add_user(self, user: User):
        db_con = sqlite3.connect(self.__database)
        cursor = db_con.cursor()

        if len(self.find_by_email(user.email)):
            raise RepoException('User already in database!')

        query = f'insert into Users values(null, "{user.username}", "{user.email}", "{user.password}")'
        cursor.execute(query)
        db_con.commit()

        db_con.close()

    def find_by_email(self, user_mail):
        db_con = sqlite3.connect(self.__database)
        cursor = db_con.cursor()

        query = f"select * from Users where email = '{user_mail}'"
        cursor.execute(query)

        result = cursor.fetchall()
        db_con.close()

        return result
