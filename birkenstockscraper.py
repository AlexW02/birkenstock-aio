import requests, time, ctypes, datetime, re, json, sqlite3
from clint.textui import colored
from threading import Lock
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore") # ignore warnings

s_print_lock = Lock()
def s_print(*a, **b): # print function with lock to prevent messy outputs and rather having a clean output line by line
        with s_print_lock:
            print(*a, **b)

ctypes.windll.kernel32.SetConsoleTitleW(f"AlexAIO[Birkenstock]") # set console title

class Birkenstock():
    def __init__(self, product):

        self.s = requests.Session() # create session
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' # user agent
        self.secChUa = '"Not?A_Brand";v="8", "Chromium";v="113", "Google Chrome";v="113"' # sec-ch-ua
        # initialize product variable
        self.product = product

        s_print("[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + f' [Birkenstock] Starting task...'))

        self.scraper()
        s_print(self.white(message="Window is closing in 10 seconds..."))
        time.sleep(10)

    # print color initialization
    def yellow(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.yellow(f' [Birkenstock] {message}'))
    
    def red(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.red(f' [Birkenstock] {message}'))

    def green(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.green(f' [Birkenstock] {message}'))

    def blue(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + colored.cyan(f' [Birkenstock] {message}'))

    def white(self, message):
        return "[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + f' [Birkenstock] {message}')

    def scraper(self):

        s_print(self.yellow(message='Scraping Product...'))

        # initialize headers
        self.headers = {
            'authority': 'www.birkenstock.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.birkenstock.com/de-en?Country=DE&Language=en',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': self.userAgent,
        }

        while True:
            try:
                r = self.s.get(self.product, headers=self.headers) # GET request to get product page
                if r.status_code == 200:
                    try:
                        soup = BeautifulSoup(r.text,"html.parser") # parse html to beautiful soup module
                        name = soup.find("meta",{"property":"og:title"})['content'].split(" |")[0] # get product name
                        pid = soup.find("span",{"class":"top-productnumber"})['data-productnumber'] # get product id
                        image = soup.find("meta",{"property":"og:image"})['content'] # get product image
                        price = float(r.text.split('<span class="price-standard">')[1].split(' ')[0].strip().replace(",",".")) # get product price
                        sizes = re.findall(r'(?<=data-size=")[^"]*', r.text) # get all product sizes even sold out ones with regex
                        sizes = "\n".join([x for x in sizes if float(x) > 30]) # join all sizes together and remove sizes below 30 to have only EU sizes in a list format so 1 size has 1 line
                        sizePids = json.loads(r.text.split(',"eans":')[1].split("}}]);")[0]) # get all product size pids with regex     
                        sizePids = "\n".join([x for x in sizePids if sizePids.index(x) < len(sizes)]) # join all size pids together and remove size pids that are not in the size list
                        conn = sqlite3.connect('products.db') # connect to products database
                        cursor = conn.cursor() # create cursor
                        cursor.execute("SELECT rowid FROM PRODUCTS WHERE PID = ?", (pid,)) # check if product is already in database
                        data=cursor.fetchall() # fetch data from database
                        if len(data) == 0: # if product is not in database
                            conn.execute(f"INSERT INTO PRODUCTS (NAME,PID,IMAGE,PRICE,SIZES,SIZE_PIDS) VALUES ('{name}', '{pid}', '{image}', {price},'{sizes}','{sizePids}')") # insert product into database
                            conn.commit() # commit changes
                        conn.close() # close connection to database
                        s_print(self.green(message=f'Successfully Scraped Product: {name} - {pid}'))
                        break
                    except Exception as e:
                        print(e)
                        s_print(self.red(message='Scrape Product: Failed to Scrape Product - Retrying...'))
                        time.sleep(2)
                elif r.status_code == 429:
                    s_print(self.red(message='Scrape Product: Rate Limited [429] - Retrying...'))
                    time.sleep(2)
                elif r.status_code == 403:
                    s_print(self.red(message='Scrape Product: Proxy Banned [403] - Retrying...'))
                    time.sleep(2)
                elif r.status_code == 404:
                    s_print(self.red(message='Scrape Product: Not Found [404] - Retrying...'))
                    time.sleep(2)
                else:
                    s_print(self.red(message=f'Scrape Product: Error [{str(r.status_code)}] - Retrying...'))
                    time.sleep(2)
            except ProxyError:
                s_print(self.red(message='Proxy Error - Retrying...'))
                time.sleep(2)
            except Exception as e:
                s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                time.sleep(2)