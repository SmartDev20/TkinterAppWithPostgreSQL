import psycopg2 as pg
from psycopg2 import Error


def connect():
    try:
        conn = pg.connect(
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port="5432",
            database="MyDB"
        )
        cur = conn.cursor()
        return conn, cur
    except(Exception, pg.DatabaseError) as error:
        print(error)
    '''finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')'''


def insert(dt, earn, exer, std, deit, pyth):
    conn = None
    cnt = 0
    try:
        get_max = 'select max(id) from routine'
        db_conn = connect()
        conn = db_conn[0]
        cur = db_conn[1]
        cur.execute(get_max)
        max_id = cur.fetchone()[0]
        max_id += 1
        # insert_qur = "INSERT INTO routine VALUES (%s , %s , %s , %s , %s , %s , %s )"
        # item_tuple = (max_id, dt, earn, exer, std, deit, pyth)
        # cur.execute(query=insert_qur, vars=(max_id, dt, earn, exer, std, deit, pyth))
        # cur.execute(insert_qur,item_tuple)
        alt_insert = f"""
        INSERT INTO routine VALUES({max_id},'{dt}',{earn},'{exer}','{std}','{deit}','{pyth}')"""
        #print(alt_insert)
        cur.execute(alt_insert)
        conn.commit()
        cnt = cur.rowcount
    except(Exception, Error) as er:
        return er
    finally:
        if conn is not None:
            conn.close()
        mesg = str(cnt) + " Records inserted successfully"
        return mesg



def create_tables():
    conn = None
    try:
        tab_create = '''
                CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , 
                earnings integer , exercise text , study text , diet text ,python text)
                '''
        db_conn = connect()
        conn = db_conn[0]
        cur = db_conn[1]
        cur.execute(tab_create)
        conn.commit()
    except(Exception, pg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_tables(dt, earn, exer, std, deit, pyth):
    conn = None
    try:
        get_max = 'select max(id) from routine'
        db_conn = connect()
        conn = db_conn[0]
        cur = db_conn[1]
        cur.execute(get_max)
        max_id = cur.fetchone()[0]
        max_id += 1
        print(type(max_id))
        insert_qur = "INSERT INTO routine VALUES (" + str(max_id) + ",'" + dt + "','" + str(earn) + "','" + exer \
                     + "','" + std + "','" + deit + "','" + pyth + "')"
        print(insert_qur)
        cur.execute(insert_qur)
        conn.commit()
    except(Exception, pg.DatabaseError) as error:
        print("from insert tables", error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def view():
    con = None
    rows = []
    try:
        seletct_qu = "SELECT * FROM routine"
        db_conn = connect()
        con = db_conn[0]
        cur = db_conn[1]
        cur.execute(seletct_qu)
        rows = cur.fetchall()
    except(Exception, Error) as er:
        return er
    finally:
        if con is not None:
            con.close()
            #print('From view : ', 'Database connection closed.')
            #print(rows)
            return rows


def delete(idx):
    con = None
    cnt = 0
    try:
        db_conn = connect()
        con = db_conn[0]
        cur = db_conn[1]
        delete_qu = "DELETE FROM routine WHERE Id = %s"
        cur.execute(delete_qu, (idx,))
        cnt = cur.rowcount
        con.commit()
    except(Exception, pg.DatabaseError) as er:
       return er
    finally:
        if con is not None:
            con.close()
            #print(cnt, "Record deleted successfully ")
            #print('From delete : ', 'Database connection closed.')
        mesg = str(cnt) + " Records deleted successfully"
        return mesg


def search(dt='', earn=None, exer='', std='', deit='', pyth=''):
    con = None
    rows = []
    try:
        db_conn = connect()
        con = db_conn[0]
        cur = db_conn[1]
        ser_qu = "SELECT * FROM routine WHERE date = %s OR  earnings = %s OR exercise = %s OR study = %s OR diet = %s " \
                 "OR python = %s "
        cur.execute(ser_qu, (dt, earn, exer, std, deit, pyth))
        rows = cur.fetchall()
    except(Exception, Error) as er:
        print(er)
    finally:
        if con is not None:
            con.close()
            print('From search : ', 'Database connection closed.')
            print(rows)
            return rows
