import sqlite3

def dbConnect(db_name) :
    conn = None
    conn = sqlite3.connect(db_name)

    return conn

def dbDisconnect(conn) :
    conn.close()

def createTable(conn, table_name, table_attribute) :
    curs = conn.cursor()
    curs.execute('''CREATE TABLE ''' + table_name + '''(''' + table_attribute + ''')''')
    conn.commit()

def tableExist(conn, table_name) :
    curs = conn.cursor()
    curs.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name=''' + table_name)
    if (curs.fetchone()[0] == 1) :
        return True
    else :
        return False

def insertTuple(conn, table_name, values) :
    curs = conn.cursor()
    curs.execute('''INSERT INTO ''' + table_name + ''' VALUES (''' + values + ''')''')
    conn.commit()

def updateTuple(conn, table_name, updates, condition) :
    curs = conn.cursor()
    curs.execute("""UPDATE """ + table_name + """ SET """ + updates + """ WHERE """ + condition)
    conn.commit()

def deleteTuple(conn, table_name, condition) :
    curs = conn.cursor()
    curs.execute('DELETE FROM ' + table_name + ' WHERE ' + condition)
    conn.commit()

def getTuple(conn, query) :
    curs = conn.cursor()
    curs.execute(query)

    return curs.fetchone()

def getTuples(conn, query, count=-1) :
    curs = conn.cursor()
    curs.execute(query)

    if (count == -1) :
        return curs.fetchall()
    else :
        return curs.fetchmany(count)