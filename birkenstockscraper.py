import requests, time, ctypes, datetime
from clint.textui import colored
from threading import Lock
from requests.exceptions import ProxyError
import warnings
warnings.filterwarnings("ignore")

s_print_lock = Lock()
def s_print(*a, **b):
        with s_print_lock:
            print(*a, **b)

ctypes.windll.kernel32.SetConsoleTitleW(f"AlexAIO[Birkenstock]")

class Birkenstock():
    def __init__(self, product):

        self.s = requests.Session()
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

        s_print("[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + f' [TASK - {self.taskNumb}] [Birkenstock] Starting task...'))



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

    def scraper(self):

        s_print(self.yellow(message='Scraping Product...'))

        self.headers = {
            'Host': 'www.birkenstock.com',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
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

        self.data = {
            'dwfrm_newsletter_email': self.email,
            'dwfrm_newsletter_firstname': '',
            'dwfrm_newsletter_lastname': '',
            'dwfrm_newsletter_acceptterms': 'true',
            'frc-captcha-solution': result,
        }

        while True:
            try:
                r = self.s.get('https://www.birkenstock.com/on/demandware.store/Sites-DE-Site/en_DE/Newsletter-SubscribeFooter?nlSignupSource=homepage', headers=self.headers, data=self.data, proxies=self.proxies)
                if r.status_code == 200:
                    if r.json()["success"] == True:
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