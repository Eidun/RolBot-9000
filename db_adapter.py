import psycopg2
import urllib.parse as urlparse
import os


class DBAdapter:
    def __init__(self, mode):
        if mode == 0:
            self.__production_connection()
        else:
            self.__test_connection()

        self.conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port)

        self.cur = self.conn.cursor()

    def __production_connection(self):
        self.url = urlparse.urlparse(os.environ['DATABASE_URL'])
        self.database = self.url.path[1:]
        self.user = self.url.username
        password = self.url.password
        host = self.url.hostname
        port = self.url.port

    def __test_connection(self):
        self.database = 'RolBot-9000'
        self.user = 'rol'
        self.password = 'rol'
        self.host = 'localhost'
        self.port = 5432

    def get_cards_db(self, identificador):
        cur = self.conn.cursor()
        statement = "SELECT * from infos where alias=%s or nombre=%s"
        cur.execute(statement, (identificador, identificador))
        rows = cur.fetchall()

        result = []
        if cur.rowcount == 0:
            result.append('0')
            result.append("not found")
        else:
            for row in rows:
                result = row
        return result
