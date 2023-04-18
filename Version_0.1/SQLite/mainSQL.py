import sqlite3 as sql



def createDB():
    conn = sql.connect("streamer.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streamer.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            name text,
            follwers integer,
            subs integers
        )"""
    )
    conn.commit()
    conn.close()


def insertROW(nombre, follwers, subs):
    conn = sql.connect("streamer.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}',{follwers},{subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()


def readROWS():
    conn = sql.connect("streamer.db")

    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)

    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


def insertROWS(streamersLIST):
    conn = sql.connect("streamer.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?,?,?)"

    cursor.executemany(instruccion,streamersLIST)

    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("streamer.db")

    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)

    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


def search():
    conn = sql.connect("streamer.db")

    cursor = conn.cursor()

    instruccion = f"SELECT * FROM streamers WHERE name = 'ibai'"
    cursor.execute(instruccion)

    datos = cursor.fetchall()

    conn.commit()
    conn.close()
    print(datos)


def updateFields():
    conn = sql.connect("streamer.db")
    cursor = conn.cursor()

    instruccion = f"UPDATE streamers SET follwers = 400 WHERE name like 'elxkas'"
    cursor.execute(instruccion)


    conn.commit()
    conn.close()


def delereROW():
    conn = sql.connect("streamer.db")

    cursor = conn.cursor()

    instruccion = f"DELETE FROM streamers WHERE name = 'ibai'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()



if __name__ == "__main__":
    # createDB()
    # createTable()
    # insertROW("ibai", 40,35)
    # insertROW("Alex el capo", 80,75)
    # readROWS()
    streamers = [
        ("ElXkas",2000,600),
        ("Cristinini",4000,3000),
        ("Auronplay",9000,600 )
    ]
    # insertROWS(streamers)
    # readROWS()
    # print("llllllllllllllllllllllllllllllllllllll")
    # readOrdered("subs")
    # search()
    # updateFields()
    delereROW()