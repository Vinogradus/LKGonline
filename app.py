import sqlite3
import math
import array as arr
import smtplib
import email.utils
from email.mime.text import MIMEText
from random import randint
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
from flask_mail import Mail, Message

from werkzeug.exceptions import abort #Для ответа 404


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ketzelbretzel'


def genMail():
    return randint(0, 1000000)

def send2fa(mailToAuth):

    print("mailToAuth =", mailToAuth)
    codeMail = randint(100, 1000000)
    msg = MIMEText('Here is yours registration code:\n' + str(codeMail))
    msg['To'] = email.utils.formataddr(('LKGservice user', mailToAuth))
    msg['From'] = email.utils.formataddr(('LKGservice', 'kir73nest@yandex.com'))
    msg['Subject'] = 'Second step of authentication'

    server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    print(f"SMTP_SSL done")
    server.login('kir73nest@yandex.com', 'jkkagykfstsmjjap')
    print(f"login done")


    try:
        res = server.sendmail('kir73nest@yandex.com', mailToAuth, msg.as_string())
    finally:
        pass

    return codeMail

def genCookie():

    cookieToRet = temp = chr(randint(33, 127))
    for x in range(15):
        temp = chr(randint(33, 127))
        cookieToRet = cookieToRet + temp

    return cookieToRet

def send_for_forgpsw(mailToAuth):

    codeMail = genCookie()
    msg = MIMEText('Here is yours new password:\n' + str(codeMail))
    msg['To'] = email.utils.formataddr(('LKGservice user', mailToAuth))
    msg['From'] = email.utils.formataddr(('LKGservice', 'kir73nest@yandex.com'))
    msg['Subject'] = 'New password'

    server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
    print(f"SMTP_SSL done")
    server.login('kir73nest@yandex.com', 'jkkagykfstsmjjap')
    print(f"login done")


    try:
        res = server.sendmail('kir73nest@yandex.com', mailToAuth, msg.as_string())
    finally:
        pass

    return codeMail



def get_db_connection(dbName):
    dbConnection = sqlite3.connect(dbName)
    dbConnection.row_factory = sqlite3.Row

    cursor = dbConnection.cursor()
    return dbConnection


# Функция нахождения наибольшего простого делителя:
def max_simple_divider(m):
    ans = 1
    d = 2
    while (d * d <= m):
        if (m % d == 0):
            ans = d
            m = m//d
        else:
            d = d + 1
    if (m > 1):
        ans = m
    return ans;
    
def oraculus(x0, x1, x2, x3):
    a = 1
    c = 1
    m = max(max(x1, x2), max(x3, x0))
    b = 1
        
    ost1 = x2 - x1
    ost2 = x3 - x2
    ost3 = x3 - x1 
    prea1 = x1 - x0
    prea2 = x2 - x1
    prea3 = x2 - x0
    while (m < 65336):
        save_b = max_simple_divider(m)
        b = save_b
        ost1s = ost1
        ost2s = ost2
        ost3s = ost3
        if(ost1s < 0):
            ost1s = m + ost1s
        if(ost2s < 0):
            ost2s = m + ost2s
        if(ost3s < 0):
            ost3s = m + ost3s
        a = b + 1
        while(a < m):
            if (prea1 >= 0 and prea2 >= 0 and prea3 >= 0):
                if((prea1 * a)%m == ost1s and (prea2 * a)%m == ost2s and (prea3 * a)%m == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            if (prea1 < 0 and prea2 >= 0 and prea3 >= 0):
                q = ((prea1 * a) / m) - 1
                if((prea1 * a) - (m*q) == ost1s and (prea2 * a)%m == ost2s and (prea3 * a)%m == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            if (prea1 >= 0 and prea2 < 0 and prea3 >= 0):
                q = ((prea2 * a) / m) - 1
                if((prea1 * a)%m == ost1s and (prea2 * a) - (m*q) == ost2s and (prea3 * a)%m == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            if (prea1 < 0 and prea2 < 0 and prea3 >= 0):
                q1 = ((prea1 * a) / m) - 1
                q2 = ((prea2 * a) / m) - 1
                if((prea1 * a) - (m*q1) == ost1s and (prea2 * a) - (m*q2) == ost2s and (prea3 * a)%m == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            if (prea1 >= 0 and prea2 >= 0 and prea3 < 0):
                q = ((prea3 * a) / m) - 1
                if((prea1 * a)%m == ost1s and (prea2 * a)%m == ost2s and (prea3 * a) - (m*q) == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            if (prea1 < 0 and prea2 >= 0 and prea3 < 0):
                q1 = ((prea1 * a) / m) - 1
                q3 = ((prea3 * a) / m) - 1
                if((prea1 * a) - (m*q1) == ost1s and (prea2 * a)%m == ost2s and (prea3 * a) - (m*q3) == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            if (prea1 >= 0 and prea2 < 0 and prea3 < 0):
                q2 = ((prea2 * a) / m) - 1
                q3 = ((prea3 * a) / m) - 1
                if((prea1 * a)%m == ost1s and (prea2 * a) - (m*q2) == ost1s and (prea3 * a) - (m*q3) == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            if (prea1 < 0 and prea2 < 0 and prea3 < 0):
                q1 = ((prea1 * a) / m) - 1
                q2 = ((prea2 * a) / m) - 1
                q3 = ((prea3 * a) / m) - 1
                if((prea1 * a) - (m*q1) == ost1s and (prea2 * a) - (m*q2) == ost1s and (prea3 * a) - (m*q3) == ost3s):
                    c = x2 - ((a * x1)%m)
                    if ( c < 0):
                        c = m + c
                    return (a*x3 + c )%m
            b = b + save_b
            a = b + 1
        m = m + 1
    return 0
    
def schet_period(a, c, m):
    	x = randint(1, m)
    	periodd = 2
    	x = (a * x + c) % m
    	nach = x
    	x = (a * x + c) % m
    	while (x!=nach):
    	    x = (a * x + c) % m
    	    if (x!=nach):
    	        periodd = periodd + 1
    	        if(periodd > (2 * m)):
    	            return periodd
    	return periodd
    	



@app.route('/', methods = ('GET', 'POST'))
def index():

    if 'user' in session:
        return redirect(url_for('create'))

    
    if request.method == 'POST':
        
        cookie = request.cookies.get('curuser', None)
        print("cookie = ", cookie)


        login = request.form['uname']
        password = request.form['psw']

        conn = get_db_connection('usersDB.db')
        users = conn.execute('SELECT user_name, password, email FROM users;').fetchall()
	
        for row in users:
            if (login == row[0] and password == row[1]):
                res = make_response(render_template('base.html'))
                res.set_cookie('curuser', login)

                name = request.cookies.get('curuser', None)
                print("cookie = ", name)

                code = send2fa(row[2])

                conn.execute("UPDATE users SET curAuthMail = ? WHERE email = ?", [code, row[2]])
                conn.commit()
                conn.close()

                EmailE = row[2]

                session['email'] = str(EmailE)

                render_template('confirmation.html', mailCur = str(EmailE))

                return redirect(url_for('confirmation'))
                  
        conn.commit()
        conn.close()
        return render_template('index.html', otv = 'Неверное имя пользователя или пароль!')

    if not request.cookies.get('curuser'):
        return render_template('index.html')
    else:
        return redirect(url_for('create'))

@app.route('/confirmation', methods = ('GET', 'POST'))
def confirmation():

    if not 'email' in session:
        return redirect(url_for('index'))

    emailCur = session.get('email', None)

    if request.method == 'POST':
        
        print ("mail = ", emailCur)

        codePage = int(request.form['mailConfCode'])

        if codePage == 0:
            conn = get_db_connection('usersDB.db')

            code = send2fa(emailCur)

            conn.execute("UPDATE users SET curAuthMail = ? WHERE email = ?", [code, emailCur])
            conn.commit()
            conn.close()
            return render_template('confirmation.html', mailCur = emailCur, otv = 'Повторное письмо было выслано на вашу почту.')



        conn = get_db_connection('usersDB.db')
        userTable = conn.execute('SELECT curAuthMail FROM users WHERE email = ?;', [emailCur]).fetchall()
        userTableCookie = conn.execute('SELECT curCookie FROM users WHERE email = ?;', [emailCur]).fetchall()

        codeTable = userTable[0][0]
        codeTable = int(codeTable)
        conn.close()

        

        if not codeTable == codePage:
            return render_template('confirmation.html', mailCur = emailCur, otv = 'Неверный код подтверждения. Повторите попытку.')

        userTableCookie = userTableCookie[0][0]
        session['user'] = str(userTableCookie)

        return redirect(url_for('create'))

    return render_template('confirmation.html', mailCur = emailCur)



@app.route('/registration', methods = ('GET', 'POST'))
def registration():

    if request.method == 'POST':
        conn = get_db_connection('usersDB.db')
        users = conn.execute('SELECT user_name FROM users;').fetchall()
        emails = conn.execute('SELECT email FROM users;').fetchall()
        
        login = request.form['uname']
        password = request.form['psw']
        email = request.form['email']
        
        for row in users:
            if(login == row[0]):
                flash('Данное имя пользователя уже зарегисрировано!')
                conn.commit()
                conn.close()
                return render_template('registration.html', otv = 'Данное имя пользователя уже зарегисрировано!')
   
        for row in emails:
            if(email == row[0]):
                flash('Данный почтовый адрес уже зарегисрирован!')
                conn.commit()
                conn.close()
                return render_template('registration.html', otv = 'Данный почтовый адрес уже зарегисрирован!')
        
        if len(password) < 6:
            conn.commit()
            conn.close()
            return render_template('registration.html', otv = 'Слишком короткий пароль! Пароль от 6 символов!')


        cookie = genCookie()
        

        conn.execute("INSERT INTO users (user_name, password, email, curCookie) VALUES (?, ?, ?, ?)",
                (login, password, email, cookie))

        conn.commit()
        conn.close()
        

        return render_template('registration.html', otv = 'Регистрация прошла успешно!')
    

    return render_template('registration.html')
    


#Создание новой последовательности
@app.route('/create', methods = ('GET', 'POST'))
def create():
    if not 'user' in session:
        return redirect(url_for('index'))


    if request.method == 'POST':
        intA = 1
        intC = 1
        intM = 1
        intNum = 10

        if (request.form['ButtonEnter'] == "Generate"):
            intA = 2
            while intA >= intM:
                intM = randint(6000, 65336)
                intC = randint(1, 65330)
                while (math.gcd(intC,intM) != 1):
                    intC = randint(1, intM - 1)
                
                intB = 1
            
                for i in range(intM - 1, 1, -1):
                    is_simple = 0
                    if (intM % i == 0):
                        for j in range(i - 1, 1, -1):
                            if (i % j == 0): 
                                is_simple = is_simple + 1
                        if (is_simple == 0):
                            intB = intB * i

                if(intM % 4 == 0 and intB % 4 != 0):
                    intB = intB * 4
                intA = intB + 1


            return render_template('create.html', var_a = intA,
                    var_c = intC, var_m = intM, var_num = intNum)

        if (request.form['ButtonEnter'] == "Enter"):

            arrayNames = ['значение a', 'значение c', 
                                'значение m', 'Количество чисел для генерации']
            assertArray = []
            assertArray = [request.form['Param_a'], request.form['Param_c'], 
                                request.form['Param_m'], request.form['Param_num']]


            index = 0
            boolCheck = False

            print("assertArray = ", assertArray)
            for value in assertArray:
                if value == '':
                    flash('Параметр \'' + arrayNames[index] + '\' пуст!')
                    boolCheck = True
                else:
                    if index == 0: intA = int(assertArray[0])
                    if index == 1: intC = int(assertArray[1])
                    if index == 2: intM = int(assertArray[2])
                    if index == 3: intNum = int(assertArray[3])

                index = index + 1
            

            if boolCheck:
                return render_template('create.html', var_a = intA,
                    var_c = intC, var_m = intM, var_num = intNum)
            b = intA - 1

            if math.gcd(intC,intM) != 1:
                flash('с и m не взаимно простые!')
                #return render_template('create.html')
                
            for i in range(intM - 1, 1, -1):
                is_simple = 0
                if (intM % i == 0):
                    for j in range(i - 1, 1, -1):
                        if (i % j == 0): 
                            is_simple = is_simple + 1
                    if (is_simple == 0):
                        if b % i != 0:
                            flash('m имеет простой делитель, не кратный b = a-1!')
                           # return render_template('power.html')
            
            if (intM % 4 == 0 and b % 4 != 0) or (intM % 4 != 0 and b % 4 == 0):
                flash('если m кратно 4, b = a-1 тоже должно быть кратно 4 (и наоборот)!')
              #  return render_template('create.html')
            
            X = arr.array('i')
            xx = randint(1, intM)
            
            X.append((intA * xx + intC)%intM)
            for i in range(1, intNum):
                X.append((intA * X[i-1] + intC)%intM)
            
            posl = ''
            for i in range(0, intNum-1):
                posl = posl + str(X[i]) + ' '
            	
            posl = posl + str(X[intNum-1])
            

            CuserCook = session.get('user', None)
            conn = get_db_connection('usersDB.db')
            Cuser = conn.execute('SELECT user_name FROM users WHERE curCookie = ?;', [CuserCook]).fetchall()
            Cuser = Cuser[0][0]
            Cuser = str(Cuser)
            conn.close()
            
            conn = get_db_connection('dataDB.db')
            conn.execute("INSERT INTO history (user_name, posledovatelnost, a, c, m) VALUES (?, ?, ?, ?, ?)",
                (Cuser, posl, intA, intC, intM))
            conn.commit()
            conn.close()
            return render_template('create.html', otv = 'Последовательность:\n' + posl + '\na = ' + str(intA) + '\nc = '+ str(intC) +'\nm = ' + str(intM) )

    return render_template('create.html')
    
#Функция нахождения пятого числа по четырём предыдущим.
@app.route('/oracle', methods = ('GET', 'POST'))
def oracle():
    if not 'user' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        x1 = int(request.form['first'])
        x2 = int(request.form['second'])
        x3 = int(request.form['third'])
        x4 = int(request.form['forth'])
        
        x5 = oraculus(x1, x2, x3, x4)
        if x5 == 0:
            flash('Не получилось (вероятнее всего, параметр m в вашей последовательности больше 65336)!')
            return render_template('oracle.html')
        
        return render_template('oracle.html', x5=x5)
        
    return render_template('oracle.html')
    
#Проверка периода.
@app.route('/period', methods=('GET', 'POST'))
def period():
    if not 'user' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        a = int(request.form['a'])
        c = int(request.form['c'])
        m = int(request.form['m'])
        b = a - 1
        
        if math.gcd(c,m) != 1:
            flash('с и m не взаимно простые!')
            #return render_template('period.html')

        for i in range(m - 1, 1, -1):
            is_simple = 0
            if (m % i == 0):
                for j in range(i - 1, 1, -1):
                    if (i % j == 0): 
                        is_simple = is_simple + 1
                if (is_simple == 0):
                    if b % i != 0:
                        flash('m имеет простой делитель, не кратный b = a-1!')
                        #return render_template('power.html')
        
        if (m % 4 == 0 and b % 4 != 0) or (m % 4 != 0 and b % 4 == 0):
            flash('если m кратно 4, b = a-1 тоже должно быть кратно 4 (и наоборот)!')
            #return render_template('period.html')
            
        per = schet_period(a, c, m)    
        if (per == m):
            otv = 'Период = ' + str(per) + '. Период ЛКГ с данными параметрами хороший, так как равен m.'
        elif (int(per) > (2 * m)):
            otv = 'Период слишком большой и не поддаётся рассчёту (должен быть равен m)!'
        else:
            otv = 'Период = ' + str(per) + '. Период ЛКГ с данными параметрами плохой, так как не равен m.'
        
        return render_template('period.html', otv=otv)
        
    return render_template('period.html')
        
#Проверка мощности.
@app.route('/power', methods=('GET', 'POST'))
def power():

    if not 'user' in session:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        a = int(request.form['a'])
        c = int(request.form['c'])
        m = int(request.form['m'])
        b = a - 1
        
        if math.gcd(c,m) != 1:
            flash('с и m не взаимно простые!')
            #return render_template('power.html')
            
        for i in range(m - 1, 1, -1):
            is_simple = 0
            if (m % i == 0):
                for j in range(i - 1, 1, -1):
                    if (i % j == 0): 
                        is_simple = is_simple + 1
                if (is_simple == 0):
                    if b % i != 0:
                        flash('m имеет простой делитель, не кратный b = a-1!')
                        #return render_template('power.html')
    
        if (m % 4 == 0 and b % 4 != 0) or (m % 4 != 0 and b % 4 == 0):
            flash('если m кратно 4, b = a-1 тоже должно быть кратно 4 (и наоборот)!')
           # return render_template('power.html')
        
        s = 0
        while ((b**s) % m != 0):
            s = s + 1
        
        if (s >= 5):
            otv = 'Мощность = ' + str(s) + '. ЛКГ с данными параметрами обладает хорошей мощностью.'
        else:
            otv = 'Мощность = ' + str(s) + '. ЛКГ с данными параметрами обладает плохой мощностью.'
        
        return render_template('power.html', otv=otv)
        
    return render_template('power.html')


@app.route('/changeinfo', methods=('GET', 'POST'))
def changeinfo():

    if not 'user' in session:
        return redirect(url_for('index'))

    CuserCook = session.get('user', None)
    conn = get_db_connection('usersDB.db')
    CuserInfo = conn.execute('SELECT user_name, email FROM users WHERE curCookie = ?;', [CuserCook]).fetchall()
    Cuser = CuserInfo[0][0]
    Cuser = str(Cuser)
    conn.close()
        
    if request.method == 'POST':
        newname = str(request.form['uname'])
        print ("newname = ", newname)
        oldUserName = Cuser

        conn = get_db_connection('usersDB.db')
        CuserInfo = conn.execute('SELECT EXISTS(SELECT user_name FROM users WHERE user_name = ?);', [newname]).fetchall()
        conn.close()

        if CuserInfo[0][0]:
            return render_template('changeinfo.html', oldname = Cuser, otv = 'Данное имя уже занято!')



        conn = get_db_connection('usersDB.db')
        conn.execute("UPDATE users SET user_name = ? WHERE curCookie = ?", [newname, CuserCook])
        CuserInfo = conn.execute('SELECT user_name, email FROM users WHERE curCookie = ?;', [CuserCook]).fetchall()
        Cuser = CuserInfo[0][0]
        Cuser = str(Cuser)
        conn.commit()
        conn.close()
        print ("Cuser = ", Cuser)
        if not Cuser == newname:
            return render_template('changeinfo.html', oldname = Cuser, otv = 'Данное имя уже занято!')
        else:
            conn = get_db_connection('dataDB.db')
            conn.execute("UPDATE history SET user_name = ? WHERE user_name = ?", [Cuser, oldUserName])
            conn.commit()
            conn.close()

            return render_template('changeinfo.html', oldname = Cuser, otv = 'Имя успешно заменено!')

        
    return render_template('changeinfo.html', oldname = Cuser)

@app.route('/changepsw', methods=('GET', 'POST'))
def changepsw():

    if not 'user' in session:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        oldpsw = str(request.form['oldpsw'])
        newpsw = str(request.form['newpsw'])

        CuserCook = session.get('user', None)
        conn = get_db_connection('usersDB.db')
        CuserInfo = conn.execute('SELECT password FROM users WHERE curCookie = ?;', [CuserCook]).fetchall()
        CuserPass = CuserInfo[0][0]
        CuserPass = str(CuserPass)
        conn.close()

        if not CuserPass == oldpsw:
            return render_template('changepsw.html', otv = "Старый пароль введён ошибочно!")
        else:
            conn = get_db_connection('usersDB.db')
            conn.execute("UPDATE users SET password = ? WHERE curCookie = ?", [newpsw, CuserCook])
            conn.commit()
            conn.close()
            return render_template('changepsw.html', otv = "Пароль изменён успешно!")
        
    return render_template('changepsw.html')

@app.route('/forgpsw', methods=('GET', 'POST'))
def forgpsw():
        
    if request.method == 'POST':
        login = str(request.form['uname'])
        email = str(request.form['email'])

        conn = get_db_connection('usersDB.db')
        CuserInfo = conn.execute('SELECT EXISTS(SELECT * FROM users WHERE user_name = ? AND email = ?);', [login, email]).fetchall()

        conn.close()

        if not CuserInfo[0][0]:
            return render_template('forgpsw.html', otv = 'Нет зарегестрированных пользователей с таким логином и адресом электронной почты!')

        newpass = send_for_forgpsw(email)
        conn = get_db_connection('usersDB.db')
        conn.execute("UPDATE users SET password = ? WHERE user_name = ?", [newpass, login])
        conn.commit()
        conn.close()

        return render_template('forgpsw.html', otv = 'Сообщение с новым паролем было направлено на вашу почту')

        
    return render_template('forgpsw.html')

@app.route('/lk', methods=('GET', 'POST'))
def lk():

    if not 'user' in session:
        return redirect(url_for('index'))

    CuserCook = session.get('user', None)

    conn = get_db_connection('usersDB.db')
    CuserInfo = conn.execute('SELECT user_name, email FROM users WHERE curCookie = ?;', [CuserCook]).fetchall()
    Cuser = CuserInfo[0][0]
    Cuser = str(Cuser)
    UserMail = CuserInfo[0][1]
    UserMail = str(UserMail)
    conn.close()



    if request.method == 'POST':
        pos = request.form['Posledovatelnost']
        a = int(request.form['Param_a'])
        c = int(request.form['Param_c'])
        m = int(request.form['Param_m'])

        conn = get_db_connection('dataDB.db')
        conn.execute('DELETE from history WHERE posledovatelnost = ? AND a = ? AND c = ? AND m = ?', [pos, a, c, m]).fetchall()


        conn.commit()
        conn.close()

    conn = get_db_connection('dataDB.db')
    history = conn.execute('SELECT * FROM history WHERE user_name = ?', [Cuser]).fetchall()
    history.reverse()
    conn.close()
        
    return render_template('lk.html', uname = Cuser, email = UserMail, history=history)


@app.route('/logout', methods=('GET', 'POST'))
def logout():
    if not 'user' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        session.pop('user', None)
        session.pop('email', None)

        return redirect(url_for('index'))


    return render_template('logout.html')
