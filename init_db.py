import sqlite3

dataConnection = sqlite3.connect('dataDB.db')
usersConnection = sqlite3.connect('usersDB.db')


with open('scriptUsers.sql') as f:
    usersConnection.executescript(f.read())


with open('scriptData.sql') as f:
    dataConnection.executescript(f.read())

usersCursor = usersConnection.cursor()

usersCursor.execute("INSERT INTO users (user_name, password, email ) VALUES (?, ?, ?)",
            ('TestUser1', 'Test', 'Test1@gmail.com')
            )

# dataConnection.execute("INSERT INTO history (user_name, posledovatelnost, a, c, m) VALUES (?, ?, ?, ?, ?)",
#             ('TestUser1', '111 111 111 222 333 111', '1', '2', '3')
#             )
            
# dataConnection.execute("INSERT INTO history (user_name, posledovatelnost, a, c, m) VALUES (?, ?, ?, ?, ?)",
#             ('TestUser1', '22 11 11 22 33 11', '4', '5', '6')
#             )

usersConnection.commit()
usersConnection.close()

dataConnection.commit()
dataConnection.close()