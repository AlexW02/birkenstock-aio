import requests, base64, time, ctypes, names, random, datetime, json
from clint.textui import colored
from random import randint
from threading import Lock
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from bs4 import BeautifulSoup
from requests.exceptions import ProxyError
import warnings
warnings.filterwarnings("ignore") # ignore warnings

s_print_lock = Lock()
def s_print(*a, **b): # print function with lock to prevent messy outputs and rather having a clean output line by line
        with s_print_lock:
            print(*a, **b)

global success
success = 0

ctypes.windll.kernel32.SetConsoleTitleW(f"AlexAIO[Birkenstock] - Success: {success}") # set console title

def incSuccess(): # increment success counter
    global success
    success += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"AlexAIO[Birkenstock] - Success: {success}")

class Birkenstock():
    def __init__(self, threadNumb):

        with open('config.json', 'r') as config_json: # load config file to get necessary data
            data = json.loads(config_json.read())
            self.mail = data['imap_mail']
            self.pw = data['imap_password']
            self.catchall = data['catchall/gmail']

        self.s = requests.Session() # create session
        self.taskNumb = str(threadNumb) # thread number
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' # user agent
        self.secChUa = '"Not?A_Brand";v="8", "Chromium";v="113", "Google Chrome";v="113"' # sec-ch-ua

        s_print("[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + f' [TASK - {self.taskNumb}] [Birkenstock] Starting task...'))

        # initialize variables
        self.fname = names.get_first_name(gender=random.choice(['male', 'female']))
        self.lname = names.get_last_name()
        if "gmail" in self.catchall: # if gmail is used, generate random dot trick email else generate random catchall email
            emails = list()
            username_length = len(self.catchall.split("@")[0])
            combinations = pow(2, username_length - 1)
            padding = "{0:0" + str(username_length - 1) + "b}"
            for i in range(0, combinations):
                bin = padding.format(i)
                full_email = ""
                for j in range(0, username_length - 1):
                    full_email += (self.catchall[j]);
                    if bin[j] == "1":
                        full_email += "."
                full_email += (self.catchall[j + 1])
                emails.append(full_email + "@gmail.com")
            self.email = random.choice(emails)
        else:
            self.email = f'{self.fname.lower()}.{self.lname.lower()}{str(randint(1000000000, 9999999999))}{self.catchall}'
        self.delay = 2

        self.proxy_handling()
        # initializing imap mail class
        from imap import Mail
        self.mailClass = Mail(self.mail,self.pw)
        # initializing discounts.txt file
        self.discounts = open('discounts.txt', 'a+') # with permission to only append not write to it
        self.discounts.seek(0) # go to start of file
        self.discounts.truncate() # truncate file to remove all content
        while True:
            resp = self.newsletter() # start newsletter function
            if resp == True:
                break
            else:
                continue

    # print color initialization
    def yellow(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.yellow(f' [TASK - {self.taskNumb}] [Birkenstock] {message}'))
    
    def red(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.red(f' [TASK - {self.taskNumb}] [Birkenstock] {message}'))

    def green(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.green(f' [TASK - {self.taskNumb}] [Birkenstock] {message}'))

    def blue(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.cyan(f' [TASK - {self.taskNumb}] [Birkenstock] {message}'))

    def white(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + f' [TASK - {self.taskNumb}] [Birkenstock] {message}')

    # proxy handling function
    def proxy_handling(self):

        with open('proxies.txt', 'r') as self.proxies_text:
            self.proxies = self.proxies_text.read().splitlines()
            if not self.proxies:
                self.proxy = ''
                self.proxy_hook = 'localhost'
            else:
                self.proxy = self.proxies[int(self.taskNumb)-1]
                self.proxy_hook = self.proxy
                try:
                    proxy_parts = self.proxy.split(":")
                    ip, port, user, passw = proxy_parts[0], proxy_parts[
                        1], proxy_parts[2], proxy_parts[3]
                    self.proxies = {
                        "http": "http://{}:{}@{}:{}".format(user, passw, ip, port)
                    }
                except IndexError:
                    self.proxies = {"http": "http://" + self.proxy, "https": "https://" + self.proxy}

    def newsletter(self):

        s_print(self.yellow(message='Launching Harvester...'))

        # initializing selenium chrome webdriver
        chromeOptions = Options()
        chromeOptions.add_argument("log-level=3") # disable console logging
        chromeOptions.add_argument("--no-sandbox") # disable sandbox mode
        chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging']) # disable chrome automation feature
        chromeOptions.add_experimental_option("detach", True) # detach chrome from python
        chromeOptions.add_argument("window-size=200,200") # set window size to 200x200
        chromeOptions.add_argument("--disable-web-security") # disable web security
        chromeOptions.add_argument(f'user-agent={self.userAgent}') # set user agent
        chromeOptions.add_experimental_option("useAutomationExtension", False) # disable chrome automation extension
        while True:
            try:
                driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=chromeOptions) # initialize chromedriver
                break
            except:
                s_print(self.red(message='Chromedriver exception - recheck your chromedriver.exe'))
                time.sleep(5)
        # html code for friendly captcha solver
        r = """
        <html>
        <head></head>
        <body>
            <div class="grid-row">
                    <div class="large-6 grid-columns li" id="checkoutAddressData">
                                                                <section id="checkout-process-captcha">
                                <script type="module" src="https://cdn.jsdelivr.net/npm/friendly-challenge@0.9.0/widget.module.min.js" async defer></script>
                                <script nomodule src="https://cdn.jsdelivr.net/npm/friendly-challenge@0.9.0/widget.min.js" async defer></script>
                                                        <div
                                    class="frc-captcha"
                                    data-sitekey="FCMVTPT64JLMNDQS"
                                    data-puzzle-endpoint="https://eu-api.friendlycaptcha.eu/api/v1/puzzle"
                                    data-callback="checkoutCaptchaCallback"
                                ></div>
                                <script>
                                    function checkoutCaptchaCallback(solution) {
                                        document.getElementById('wait2').style.display = 'block';
                                        jQuery('#checkoutForm').submit();
                                        jQuery('#checkout-process-captcha').fadeOut();
                                    }
                                </script>
                            </section>
                                    </div>
        </body>
        </html>
        """
        stealth(
                    driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="MacIntel",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                ) # initialize selenium stealth
        html = base64.b64encode(r.encode('utf-8')).decode() # encode html code to base64 encoded string to be able to be opened by selenium
        driver.get("data:text/html;base64," + html) # open html code im selenium browser

        notified = False
        # monitoring page source until captcha is available
        while True:
            try:
                driver.find_element(By.CLASS_NAME, "frc-button").click()
                break
            except:
                continue
        # monitoring page source until captcha is solved
        while True:
            soup = BeautifulSoup(driver.page_source,"html.parser")
            if "UNFINISHED" not in soup.find("input",{"name":"frc-captcha-solution"})['value'] and "UNSTARTED" not in soup.find("input",{"name":"frc-captcha-solution"})['value'] and "FETCHING" not in soup.find("input",{"name":"frc-captcha-solution"})['value'] and len(soup.find("input",{"name":"frc-captcha-solution"})['value']) >25: # check if captcha is actually solved
                result = soup.find("input",{"name":"frc-captcha-solution"})['value'] # get captcha token by beautiful soup html parser
                s_print(self.blue(message='Successfully Retrieved Captcha Token!'))
                break
            else:
                if notified == False:
                    notified = True 
                    s_print(self.yellow(message='Waiting for Captcha Result...'))
                time.sleep(2)
        try:
            driver.quit()
        except:
            pass

        s_print(self.yellow(message='Subscribing To Newsletter...'))

        # initializing headers
        self.headers = {
            'sec-ch-ua': self.secChUa,
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': self.userAgent,
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://www.birkenstock.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.birkenstock.com/de-en',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        # initializing data
        self.data = {
            'dwfrm_newsletter_email': self.email,
            'dwfrm_newsletter_firstname': '',
            'dwfrm_newsletter_lastname': '',
            'dwfrm_newsletter_acceptterms': 'true',
            'frc-captcha-solution': result,
        }

        while True:
            try:
                r = self.s.post('https://www.birkenstock.com/on/demandware.store/Sites-DE-Site/en_DE/Newsletter-SubscribeFooter?nlSignupSource=homepage', headers=self.headers, data=self.data, proxies=self.proxies) # POST request to subscribe to newsletter
                if r.status_code == 200:
                    if r.json()["success"] == True: # check if newsletter subscription was successful
                        s_print(self.yellow(message='Successfully Subscribed To Newsletter!'))
                        break
                    else:
                        s_print(self.red(message='Subscription Failed - Retrying...'))
                        return False
                elif r.status_code == 429:
                    s_print(self.red(message='Newsletter: Rate Limited [429] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 403:
                    s_print(self.red(message='Newsletter: Proxy Banned [403] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 404:
                    s_print(self.red(message='Newsletter: Not Found [404] - Retrying...'))
                    time.sleep(self.delay)
                else:
                    s_print(self.red(message=f'Newsletter: Error [{str(r.status_code)}] - Retrying...'))
                    time.sleep(self.delay)
            except ProxyError:
                s_print(self.red(message='Proxy Error - Retrying...'))
                time.sleep(self.delay)
                continue
            except Exception as e:
                s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                time.sleep(self.delay)

        # using imap.py to monitor inbox of the gmail until the verification email is received
        s_print(self.white(message="Waiting for Email..."))
        self.link = None
        while self.link == None:
            self.link = self.mailClass.getLink(self.email) # get verification link from email
            if self.link == None:
                time.sleep(2)
                continue
            s_print(self.blue(message=f"Retrieved Link: {self.link}"))
            break
        
        s_print(self.yellow(message='Verifying Email...'))

        while True:
            try:
                r = self.s.get(self.link, proxies=self.proxies) # GET request to verify email
                if r.status_code == 200:
                    s_print(self.yellow(message='Successfully Verified Email!'))
                    break
                elif r.status_code == 429:
                    s_print(self.red(message='Verify Email: Rate Limited [429] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 403:
                    s_print(self.red(message='Verify Email: Proxy Banned [403] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 404:
                    s_print(self.red(message='Verify Email: Not Found [404] - Retrying...'))
                    time.sleep(self.delay)
                else:
                    s_print(self.red(message=f'Verify Email: Error [{str(r.status_code)}] - Retrying...'))
                    print(r.text)
                    time.sleep(self.delay)
            except ProxyError:
                s_print(self.red(message='Proxy Error - Retrying...'))
                time.sleep(self.delay)
                continue
            except Exception as e:
                s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                time.sleep(self.delay)

        # using imap.py to monitor inbox of the gmail until the discount code email is received
        s_print(self.white(message="Waiting for Email..."))
        self.code = None
        while self.code == None:
            self.code = self.mailClass.getEmail(self.email) # get discount code from email
            if self.code == None:
                time.sleep(2)
                continue
            self.discounts.write(f"{self.code}\n") # append discount code to discounts.txt file
            s_print(self.green(message=f"Retrieved Discount Code: {self.code}"))
            incSuccess()
            return True