



import smtplib
import email.utils
from email.mime.text import MIMEText
'''

def genCookie():

    cookieToRet = ""
    for x in range(16):
        temp = chr(randint(33, 127))
        print(f"temp = {temp}")
        cookieToRet = cookieToRet + temp
    # for x in range(16):
    #     cookieToRet = cookieToRet + 

    return cookieToRet'''


# res = genCookie()
# print(f"res = {res}")


# s = smtplib.SMTP('localhost')
# msg['Subject'] = 'The contents of %s' % textfile
# msg['From'] = me
# msg['To'] = you
msg = MIMEText("fp.read()")
# s.quit()



# cc = 'chris@*************.com'
# msg['Cc'] = cc
# server = smtplib.SMTP_SSL('gator3119.hostgator.com:465')
# print(f"SMTP_SSL done")
# toaddr = 'ruslan_f_f@mail.ru'
# fromaddr = "ivantitivan@mail.ru"

# server.login(fromaddr, ";(3;@($HF*")
# print(f"login done")
# text = msg.as_string()

# server.sendmail(fromaddr, toaddr, text)
# server.quit()


# --- create our message ---

# Create our message. 
msg = MIMEText('The body of your message.')
msg['To'] = email.utils.formataddr(('Recipient Name', 'daniilprotasove@gmail.com'))
msg['From'] = email.utils.formataddr(('LKGservice', 'kir73nest@yandex.com'))
msg['Subject'] = 'Privet'

print("msg: ", msg)

# --- send the email ---

# server = smtplib.SMTP_SSL()
# server = smtplib.SMTP()
# print(f"SMTP done")
# server.connect ('smtp.mail.ru', 465)
# print(f"connect done")

# server = smtplib.SMTP_SSL('smtp.mail.com', 465)
# print(f"SMTP_SSL done")
# # server.starttls()
# server.login('ivantitivan@mail.ru', 'eKCuANNjVi673PTqxjrN')
# print(f"login done")


server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
print("SMTP_SSL done")
# server.starttls()
server.login('kir73nest@yandex.com', 'jkkagykfstsmjjap')
print("login done")

# Optional login for the receiving mail_server.
# server.login ('login@example.com', 'Password')

# Dump communication with the receiving server straight to to the console.
# server.set_debuglevel(True)  

# 'yourname@yourdomain.com' is our envelope address and specifies the return
# path for bounced emails.
try:
    # BIP eKCuANNjVi673PTqxjrN
    res = server.sendmail('kir73nest@yandex.com', ['daniilprotasove@gmail.com'], msg.as_string())
    print("sendmail good", res)
finally:
    print("sendmail quit1")
    server.quit()
    print("sendmail quit2")




























