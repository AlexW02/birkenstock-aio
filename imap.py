from imap_tools import MailBox,AND
import time
import threading
emails = None
codeDatabase = {}
linkDatabase = {}
class Mail:
    def __init__(self,email,pw):
        self.absender = "news_de@europe.birkenstock.com"
        self.email = email
        self.password = pw
        self.imap = "imap.gmail.com"
        threading.Thread(target=self.fetchEmails).start()
    def getEmail(self,email):
        if email in codeDatabase:
            return codeDatabase[email]
        else:
            return None
    def getLink(self,email):
        if email in linkDatabase:
            return linkDatabase[email]
        else:
            return None
    def fetchEmails(self):
        global emails
        while True:
            try:
                mail = MailBox(self.imap,port="993")
                mail.login(self.email,self.password)
                emails = mail.fetch(criteria=AND(seen=False, from_=self.absender),
                            mark_seen=True,
                            bulk=True)
                for msg in emails:
                    to = msg.to[0]
                    if '"_blank">HIER BESTÄTIGEN</a>' in msg.html:
                        try:
                            link = msg.html.split('"_blank">HIER BESTÄTIGEN</a>')[0].split('<a  href="')[-1].split('"')[0]
                            linkDatabase[to] = link
                        except:
                            pass
                    else:
                        try:
                            code = msg.html.split('Dein 10-€-Gutscheincode* für deinen Einkauf in unserem Online-Shop:<br><br><b>')[1].split('<')[0]
                            codeDatabase[to] = code
                        except:
                            link = msg.html.split('<a href="')[1].split('"')[0].replace("\n", "")
                            linkDatabase[to] = link
                            pass
            except:
                import traceback
                tr = str(traceback.format_exc()).lower()
                if "invalid" in tr:
                    print("Invalid IMAP Data! Please make sure you have the correct APP password!")
                    return
                elif "please" in tr:
                    print("Please login with your email account on your current server / pc!")
                    return
            mail.logout()
            time.sleep(3)