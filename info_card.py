import psycopg2
import urllib.parse as urlparse
import os
class InfoCard:

    def __init__(self, name: str):
        self.name = name
        self.get_card()

    def get_card(self):

        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        database = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port
        """
        database = 'RolBot-9000'
        user = 'rol'
        password = 'rol'
        host = 'localhost'
        port = 5432
        """
        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port)

        cur = conn.cursor()
        statement = "SELECT * from infos where nombre=%s"
        cur.execute(statement, (self.name,))
        print(cur.rowcount)
        rows = cur.fetchall()

        result = []
        if cur.rowcount == 0:
            result.append('0')
            result.append("not found")
        else:
            for row in rows:
                result = row
        return result

