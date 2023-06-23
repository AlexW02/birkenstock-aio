from imap_tools import MailBox,AND
import time
import threading
emails = None
codeDatabase = {}
linkDatabase = {}
class Mail: # imap Mail class
    def __init__(self,email,pw):
        self.absender = "news_de@europe.birkenstock.com" # sender email
        self.email = email # email which should be used
        self.password = pw # gmail app password
        self.imap = "imap.gmail.com" # imap server initialization
        threading.Thread(target=self.fetchEmails).start() # starting thread
    def getEmail(self,email): # get email for discount code
        if email in codeDatabase: # if email is in database already
            return codeDatabase[email]
        else:
            return None
    def getLink(self,email): # get email for verification link
        if email in linkDatabase: # if email is in database already
            return linkDatabase[email]
        else:
            return None
    def fetchEmails(self):
        global emails # global variable for all emails
        while True:
            try:
                mail = MailBox(self.imap,port="993") # imap mailbox initialization
                mail.login(self.email,self.password) # login with email and app password
                emails = mail.fetch(criteria=AND(seen=False, from_=self.absender), # fetch emails from defined sender
                            mark_seen=True,
                            bulk=True)
                for msg in emails: # iterate over emails
                    to = msg.to[0]
                    if '"_blank">HIER BESTÄTIGEN</a>' in msg.html: # if email is verification email
                        try:
                            link = msg.html.split('"_blank">HIER BESTÄTIGEN</a>')[0].split('<a  href="')[-1].split('"')[0] # get verification link
                            linkDatabase[to] = link # add to database
                        except:
                            pass
                    else: # if email is discount email
                        try:
                            code = msg.html.split('Dein 10-€-Gutscheincode* für deinen Einkauf in unserem Online-Shop:<br><br><b>')[1].split('<')[0] # get discount code
                            codeDatabase[to] = code # add to database
                        except:
                            link = msg.html.split('<a href="')[1].split('"')[0].replace("\n", "")
                            linkDatabase[to] = link
                            pass
            except:
                import traceback
                tr = str(traceback.format_exc()).lower()
                if "invalid" in tr:
                    print("Invalid IMAP Data! Please make sure you have the correct APP password!") # if imap data is invalid
                    return
                elif "please" in tr:
                    print("Please login with your email account on your current server / pc!") # if imap data is invalid
                    return
            mail.logout()
            time.sleep(3)