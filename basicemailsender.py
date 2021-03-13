import smtplib

class MailService:
# Variables:
    # Hided data:
    __mailServer = ""
    __port = 0
    __sender = ""
    __passWord = ""
    # Public data:
    receivers = []
    emailContent = ""

# Hided Methods:
    # Constructor:
    def __init__(self, inputSenderAddr, inputpassWd, inputServer = 'smtp.gmail.com', inputPort = 587):
        #
        self.__mailServer = inputServer
        self.__port = inputPort
        self.__sender = inputSenderAddr
        self.__passWord = inputpassWd
    
# Interface
    # Send email
    def emailSender(self):
    #
        smtpObj = smtplib.SMTP(self.__mailServer, self.__port)
        smtpObj.ehlo()
        smtpObj.starttls()
    
        try:
            smtpObj.login(self.__sender, self.__passWord)
    
            try:
                smtpObj.sendmail(self.__sender, self.receivers, self.emailContent)
                print ("Send successful")
            finally:
                smtpObj.quit()

        except Exception:
            print ("Error: Cannot send email")
