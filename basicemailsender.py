import smtplib

sender = 'youremailaddres@gmail.com'
receivers = ['receiveremailaddres@gmail.com']

message = """From: <youremailaddres@gmail.com>
To: <receiveremailaddres@gmail.com>
Subject: SMTP e-mail test

Day la vi du ve gui email.
"""

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

try:
    smtpObj.login('youremailaddres@gmail.com', 'youremailpassword')
    
    try:
        smtpObj.sendmail(sender, receivers, message)
        print ("Send successful")
    finally:
        smtpObj.quit()

except Exception:
    print ("Error: Cannot send email")