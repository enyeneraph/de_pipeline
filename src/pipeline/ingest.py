import psycopg2

def connect_db(user, password, host, database, port):
    conn = psycopg2.connect(user=user,
                            password=password,
                            host=host,
                            database=database,
                            port=port)
    return conn

def insert_sql(row, table_name='jobs.jobs'):
    fields = ', '.join(row.keys())
    placeholders = ', '.join(["%({})s".format(k) for k in row.keys()])
    sql = "INSERT INTO {table_name} ({fields}) VALUES ({values});"
    return sql.format(table_name=table_name, fields=fields, values=placeholders)



def insert_data(conn, row):
    """ Inserts one row in a transaction"""
    SQL = insert_sql(row)
    with conn.cursor() as curs:
        curs.execute(SQL, row)
    conn.commit() 

def fetch_data(conn, query, values):
    with conn.cursor() as curs:
        curs.execute(query, values)
        tp = curs.fetchone()
        return None if tp is None else tp[0]


