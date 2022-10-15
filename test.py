'''import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    history = conn.execute('SELECT posledovatelnost FROM history').fetchall()
    print (history)
    conn.close()
    return 1
    
    
index()'''

import sqlite3

def get_db_connection(dbName):
    dbConnection = sqlite3.connect(dbName)
    dbConnection.row_factory = sqlite3.Row

    cursor = dbConnection.cursor()
    return dbConnection

conn = get_db_connection('usersDB.db')
name = 'TestUser1'
pas = 'Test4'
mail = 'Test1@gmail.com'
#conn.execute("INSERT INTO users (user_name, password, email) VALUES (?, ?, ?)",
#            (name, pas, mail)
#            )
users = conn.execute('SELECT curAuthMail FROM users WHERE email = ? ', [mail]).fetchall()
print(users[0][0])

name = 'TestUser1'
code = 111

conn.execute("UPDATE users SET curAuthMail = ? WHERE user_name = ?", [code, name])

users = conn.execute('SELECT * FROM users ').fetchall()
for user in users:
    print(user)

emailCur = 'daniilprotasove@gmail.com'

userTable = conn.execute('SELECT curAuthMail FROM users WHERE email = ?;', [emailCur]).fetchall()

codeTable = userTable[0][0]
print(codeTable)

codeTable = int(codeTable) 
if codeTable == 724946:
    print('OK')

conn.commit()
conn.close()

conn = get_db_connection('dataDB.db')
history = conn.execute('SELECT * FROM history').fetchall()
print (history)
print ("Naoborot")
history.reverse()
print(history)
conn.close()

print (" ")

login = "PRDaniilPR"
email = "daniilprotasove@gmail.com"

conn = get_db_connection('usersDB.db')
CuserInfo = conn.execute('SELECT EXISTS(SELECT * FROM users WHERE user_name = ? AND email = ?);', [login, email]).fetchall()
if CuserInfo[0][0]:
    print('1DOLZNO')
if not CuserInfo[0][0]:
    print('1NE DOLZNO')

login = "aniilPR"
email = "dlprotasove@gmail.com"

CuserInfo = conn.execute('SELECT EXISTS(SELECT * FROM users WHERE user_name = ? AND email = ?);', [login, email]).fetchall()
conn.close()
if CuserInfo[0][0]:
    print('2NE DOLZNO')
if not CuserInfo[0][0]:
    print('2 DOLZNO')