# Работаем с модулем psycopg2 для подключения к PostgreSQL
# Импортируем настройки из config
# Получаем версию PostgreSQL
import psycopg2
from config import config


def connect():
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)

    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()


connect()
