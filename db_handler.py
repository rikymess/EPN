import sqlite3

def register(name, lastname, mail, time, signal):
    con = sqlite3.connect('/home/riktymes/Desktop/EPN/epn/include/users')
    cur = con.cursor()
    cur.execute(f"INSERT INTO users (name, lastname, mail, time) VALUES ( '{name}', '{lastname}', '{mail}', '{time}')")
    signal.emit('Merci!')
    con.commit()
    cur.close()
    con.close()
    





