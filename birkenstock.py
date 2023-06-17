import requests, time, json, datetime, random, names, string, re, ctypes, urllib3
from discord_webhook import DiscordWebhook, DiscordEmbed
from random import randint
from threading import Lock
from requests.exceptions import ProxyError
from clint.textui import colored
urllib3.disable_warnings()

s_print_lock = Lock()
def s_print(*a, **b):
        with s_print_lock:
            print(*a, **b)

global carted 
global success
carted = 0
success = 0

ctypes.windll.kernel32.SetConsoleTitleW(f"AlexAIO[Birkenstock] - Carted: {carted} | Success: {success}")

def incCart():
    global carted
    carted += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"AlexAIO[Birkenstock] - Carted: {carted} | Success: {success}")

def incSuccess():
    global success
    success += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"AlexAIO[Birkenstock] - Carted: {carted} | Success: {success}")

class Birkenstock():
    def __init__(self, pid, email, fname, lname, address, number, phone, postcode, city, region, discount, delay, webhook, threadNumb):

        self.s = requests.Session()
        self.taskNumb = str(threadNumb)
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        self.secChUa = '"Not?A_Brand";v="8", "Chromium";v="113", "Google Chrome";v="113"'

        s_print("[" + (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3] + "]" + f' [TASK - {self.taskNumb}] [Birkenstock] Starting Task...'))

        self.pid = pid
        self.fname = fname
        if self.fname.lower() == "random":
            self.fname = names.get_first_name(gender=random.choice(['male', 'female']))
        self.lname = lname
        if self.lname.lower() == "random":
            self.lname = names.get_last_name()
        self.email = email
        if "random" in self.email.lower():
            self.email = self.email.lower().replace('random', f'{self.fname}.{self.lname}{str(randint(1000000000, 9999999999))}')
        self.address = address
        self.address = self.address.replace('XXX', ''.join(random.choice(string.ascii_letters) for x in range(3)).upper())
        self.number = number
        self.phone = phone
        if self.phone.lower() == 'random':
            self.phone = str(random.randint(1000000000, 9999999999))
        self.postcode = postcode
        self.city = city
        self.region = region
        self.discount = discount
        self.delay = int(delay)
        self.webhook = webhook
        self.preload = True
        self.dummies = ["4052001745264","4052001745301","4052001745349","4052001745387","4052001745424","4052001745462","4052001745509","4052001745547","4052001745585","4052001745622","4052001745660","4052001745707","4052001745745","4052001745783","4052001745820","4052001745868","4052001745905","4052001745943","4052001745981","4052001746025","4052001746063","4052001746100"]

        while True:
            try:
                self.proxy_handling()
                self.atcDummy()
                self.checkout()
                self.clearCart()
                self.atc()
                self.preload = False
                self.checkout()
                break
            except Exception as e:
                s_print(self.red(message=f"System Error - {e}"))
        s_print(self.white(message="Window is closing in 10 seconds..."))
        time.sleep(10)

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

    def atcDummy(self):

        s_print(self.yellow(message='Preloading...'))

        self.headers = {
            'Host': 'www.birkenstock.com',
            'sec-ch-ua': self.secChUa,
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': self.userAgent,
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://www.birkenstock.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.birkenstock.com/',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        self.data = {
            'productCurrency': 'EUR',
            'cartAction': 'add',
            'pid': self.pid,
            'groupSize': 'null',
            'Quantity': '1',
        }

        while True:
            self.dummy = random.choice(self.dummies)
            self.data['pid'] = self.dummy
            try:
                r = self.s.post('https://www.birkenstock.com/on/demandware.store/Sites-DE-Site/en_DE/Cart-AddProduct?format=ajax', headers=self.headers, data=self.data, proxies=self.proxies)
                if r.status_code == 200:
                    if '<span class="mini-cart-quantity">\n1' in r.text:
                        break
                    else:
                        s_print(self.red(message='Failed To Add To Cart Dummy - Retrying...'))
                        time.sleep(self.delay)
                elif r.status_code == 429:
                    s_print(self.red(message='Dummy ATC: Rate Limited [429] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 403:
                    s_print(self.red(message='Dummy ATC: Proxy Banned [403] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 404:
                    s_print(self.red(message='Dummy ATC: Not Found [404] - Retrying...'))
                    time.sleep(self.delay)
                else:
                    s_print(self.red(message=f'Dummy ATC: Error [{str(r.status_code)}] - Retrying...'))
                    time.sleep(self.delay)
            except ProxyError:
                s_print(self.red(message='Proxy Error - Retrying...'))
                time.sleep(self.delay)
                continue
            except Exception as e:
                s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                time.sleep(self.delay)

    def clearCart(self):

        self.headers = {
            'Host': 'www.birkenstock.com',
            'sec-ch-ua': self.secChUa,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'user-agent': self.userAgent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        while True:
            try:
                r = self.s.get('https://www.birkenstock.com/de-en/cart', headers=self.headers, proxies=self.proxies)
                if r.status_code == 200:
                    try:
                        url = r.text.split('<form action="')[2].split('"')[0]
                        totalPrice = r.text.split('<input type="hidden" name="basePrice" value="')[1].split('"')[0]
                        break
                    except:
                        s_print(self.red(message='Failed To Get Cart - Retrying...'))
                        time.sleep(self.delay)
                        continue
                elif r.status_code == 429:
                    s_print(self.red(message='Get Cart: Rate Limited [429] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 403:
                    s_print(self.red(message='Get Cart: Proxy Banned [403] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 404:
                    s_print(self.red(message='Get Cart: Not Found [404] - Retrying...'))
                    time.sleep(self.delay)
                else:
                    s_print(self.red(message=f'Get Cart: Error [{str(r.status_code)}] - Retrying...'))
                    time.sleep(self.delay)
            except ProxyError:
                s_print(self.red(message='Proxy Error - Retrying...'))
                time.sleep(self.delay)
                continue
            except Exception as e:
                s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                time.sleep(self.delay)
                continue

        if self.discount != "":

            s_print(self.yellow(message='Applying Discount...'))

            self.headers = {
                'Host': 'www.birkenstock.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': self.secChUa,
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'origin': 'https://www.birkenstock.com',
                'user-agent': self.userAgent,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://www.birkenstock.com/de-en/cart',
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            self.data = {
                'minicartPid': self.dummy,
                'dwfrm_cart_shipments_i0_items_i0_quantity': '1',
                'totalPrice': totalPrice,
                'dwfrm_cart_couponCode': self.discount,
                'dwfrm_cart_addCoupon': 'dwfrm_cart_addCoupon',
            }

            while True:
                try:
                    r = self.s.post(url, headers=self.headers, data=self.data, proxies=self.proxies)
                    if r.status_code == 200:
                        if '<span class="applied">Applied</span>' in r.text:
                            try:
                                url = r.text.split('<form action="')[2].split('"')[0]
                                s_print(self.blue(message='Successfully Applied Discount!'))
                                break
                            except:
                                s_print(self.red(message='Failed To Apply Discount - Retrying...'))
                                time.sleep(self.delay)
                                continue
                        else:
                            s_print(self.red(message='Failed To Apply Discount - Continuing...'))
                            break
                    elif r.status_code == 429:
                        s_print(self.red(message='Apply Discount: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 403:
                        s_print(self.red(message='Apply Discount: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 404:
                        s_print(self.red(message='Apply Discount: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Apply Discount: Error [{str(r.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)

        s_print(self.yellow(message='Clearing Cart...'))

        self.headers = {
            'Host': 'www.birkenstock.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': self.secChUa,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://www.birkenstock.com',
            'user-agent': self.userAgent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': r.url,
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        self.data = {
            'minicartPid': self.dummy,
            'dwfrm_cart_shipments_i0_items_i0_quantity': '1',
            'dwfrm_cart_shipments_i0_items_i0_deleteProduct': 'Remove',
            'totalPrice': totalPrice,
            'dwfrm_cart_couponCode': '',
        }

        while True:
            try:
                r = self.s.post(url, headers=self.headers, data=self.data, proxies=self.proxies)
                if r.status_code == 200:
                    if '<span>You have no items in your shopping cart</span>' in r.text:
                        break
                    else:
                        s_print(self.red(message='Failed To Clear Cart - Retrying...'))
                        time.sleep(self.delay)
                elif r.status_code == 429:
                    s_print(self.red(message='Clear Cart: Rate Limited [429] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 403:
                    s_print(self.red(message='Clear Cart: Proxy Banned [403] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 404:
                    s_print(self.red(message='Clear Cart: Not Found [404] - Retrying...'))
                    time.sleep(self.delay)
                else:
                    s_print(self.red(message=f'Dummy ATC: Error [{str(r.status_code)}] - Retrying...'))
                    time.sleep(self.delay)
            except ProxyError:
                s_print(self.red(message='Proxy Error - Retrying...'))
                time.sleep(self.delay)
                continue
            except Exception as e:
                s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                time.sleep(self.delay)

    def atc(self):

        s_print(self.yellow(message='Adding To Cart...'))

        self.headers = {
            'Host': 'www.birkenstock.com',
            'sec-ch-ua': self.secChUa,
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': self.userAgent,
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://www.birkenstock.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.birkenstock.com/de-en/arizona-birko-flor/arizona-core-birkoflor-0-eva-u_10.html?dwvar_arizona-core-birkoflor-0-eva-u__10_width=N&dwvar_arizona-core-birkoflor-0-eva-u__10_size=290&region=EU',
            'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        self.data = {
            'productCurrency': 'EUR',
            'cartAction': 'add',
            'pid': self.pid,
            'groupSize': 'null',
            'Quantity': '1',
        }

        while True:
            try:
                r = self.s.post('https://www.birkenstock.com/on/demandware.store/Sites-DE-Site/en_DE/Cart-AddProduct?format=ajax', headers=self.headers, data=self.data, proxies=self.proxies)
                if r.status_code == 200:
                    if '<span class="mini-cart-quantity">\n1' in r.text:
                        try:
                            self.name = r.text.split('.html" title="')[1].split('"')[0]
                        except:
                            self.name = 'N/A'
                        try:
                            self.size = r.text.split('<li class="attribute" data-attribute="size">')[1].split('<span class="value">\n')[1].split('\n')[0]
                        except:
                            self.size = 'N/A'
                        try:
                            self.price = r.text.split('<span class="price-sales">')[1].split(' ')[0]+"€"
                        except:
                            self.price = 'N/A'
                        try:
                            self.image = r.text.split('<img src="')[1].split('"')[0]
                        except:
                            self.image = "https://www.birkenstock.com/on/demandware.static/Sites-DE-Site/-/default/dwcc26e7d6/images/logo.png"
                        data = json.loads(r.text.split('dataLayer.push({ "cartProducts" : [')[1].split(']')[0])
                        self.html = data["id"]
                        self.color = data["color"]
                        s_print(self.blue(message='Successfully Added To Cart!'))
                        incCart()
                        break
                    else:
                        s_print(self.red(message='Failed To Add To Cart - Retrying...'))
                        time.sleep(self.delay)
                elif r.status_code == 429:
                    s_print(self.red(message='ATC: Rate Limited [429] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 403:
                    s_print(self.red(message='ATC: Proxy Banned [403] - Retrying...'))
                    time.sleep(self.delay)
                elif r.status_code == 404:
                    s_print(self.red(message='ATC: Not Found [404] - Retrying...'))
                    time.sleep(self.delay)
                else:
                    s_print(self.red(message=f'ATC: Error [{str(r.status_code)}] - Retrying...'))
                    time.sleep(self.delay)
            except ProxyError:
                s_print(self.red(message='Proxy Error - Retrying...'))
                time.sleep(self.delay)
                continue
            except Exception as e:
                s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                time.sleep(self.delay)
                continue

    def checkout(self):

        if self.preload == True:
            self.headers = {
                'Host': 'www.birkenstock.com',
                'sec-ch-ua': self.secChUa,
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': self.userAgent,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            while True:
                try:
                    r = self.s.get('https://www.birkenstock.com/de-en/cart', headers=self.headers, proxies=self.proxies)
                    if r.status_code == 200:
                        try:
                            user = r.text.split('<input class="input-text input-email email required" id="')[1].split('"')[0]
                            pw = r.text.split('<input class="input-text input-password required" id="')[1].split('"')[0]
                            securekey = r.text.split('<input type="hidden" name="dwfrm_login_securekey" value="')[1].split('"')[0]
                            csrf = r.text.split('<input type="hidden" name="csrf_token" value="')[1].split('"')[0]
                            break
                        except:
                            s_print(self.red(message='Failed To Get Cart - Retrying...'))
                            time.sleep(self.delay)
                            continue
                    elif r.status_code == 429:
                        s_print(self.red(message='Get Cart: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 403:
                        s_print(self.red(message='Get Cart: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 404:
                        s_print(self.red(message='Get Cart: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Get Cart: Error [{str(r.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)
                    continue

            self.headers = {
                'Host': 'www.birkenstock.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': self.secChUa,
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'origin': 'https://www.birkenstock.com',
                'user-agent': self.userAgent,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://www.birkenstock.com/de-en/cart',
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            self.data = [
                ('dwfrm_cart_guestCheckout', 'true'),
                (user, ''),
                (pw, ''),
                ('dwfrm_login_securekey', securekey),
                ('csrf_token', csrf),
                ('dwfrm_cart_checkoutCart', 'dwfrm_cart_checkoutCart'),
                ('csrf_token', csrf),
            ]

            while True:
                try:
                    r = self.s.post('https://www.birkenstock.com/on/demandware.store/Sites-DE-Site/en_DE/Login-CartLogin', headers=self.headers, data=self.data, proxies=self.proxies)
                    if r.status_code == 200:
                        if 'https://www.birkenstock.com/de-en/checkout' == r.url:
                            try:
                                url = r.text.split('<form action="')[1].split('"')[0]
                                securekey = r.text.split('<input type="hidden" name="dwfrm_singleshipping_securekey" value="')[1].split('"')[0]
                                break
                            except:
                                s_print(self.red(message='Failed To Launch Checkout - Retrying...'))
                                time.sleep(self.delay)
                        else:
                            s_print(self.red(message='Failed To Launch Checkout - Retrying...'))
                            time.sleep(self.delay)
                    elif r.status_code == 429:
                        s_print(self.red(message='Launch Checkout: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 403:
                        s_print(self.red(message='Launch Checkout: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 404:
                        s_print(self.red(message='Launch Checkout: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Launch Checkout: Error [{str(r.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)
                    continue

            self.headers = {
                'Host': 'www.birkenstock.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': self.secChUa,
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'origin': 'https://www.birkenstock.com',
                'user-agent': self.userAgent,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://www.birkenstock.com/de-en/checkout',
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            self.data = {
                'dwfrm_singleshipping_shippingAddress_addressFields_salutation': 'Mr',
                'dwfrm_singleshipping_shippingAddress_addressFields_firstName': self.fname,
                'dwfrm_singleshipping_shippingAddress_addressFields_lastName': self.lname,
                'dwfrm_singleshipping_shippingAddress_addressFields_areaCode': '+49',
                'dwfrm_singleshipping_shippingAddress_addressFields_phone': '',
                'dwfrm_singleshipping_shippingAddress_addressFields_address1': self.address,
                'dwfrm_singleshipping_shippingAddress_addressFields_streetNo': self.number,
                'dwfrm_singleshipping_shippingAddress_addressFields_address2': '',
                'dwfrm_singleshipping_shippingAddress_addressFields_postal': self.postcode,
                'dwfrm_singleshipping_shippingAddress_addressFields_city': self.city,
                'dwfrm_singleshipping_billingAddress_addressFields_salutation': '',
                'dwfrm_singleshipping_billingAddress_addressFields_firstName': '',
                'dwfrm_singleshipping_billingAddress_addressFields_lastName': '',
                'dwfrm_singleshipping_billingAddress_addressFields_areaCode': '+49',
                'dwfrm_singleshipping_billingAddress_addressFields_phone': '',
                'dwfrm_singleshipping_billingAddress_addressFields_address1': '',
                'dwfrm_singleshipping_billingAddress_addressFields_streetNo': '',
                'dwfrm_singleshipping_billingAddress_addressFields_address2': '',
                'dwfrm_singleshipping_billingAddress_addressFields_postal': '',
                'dwfrm_singleshipping_billingAddress_addressFields_city': '',
                'dwfrm_singleshipping_billingAddress_addressFields_country': 'DE',
                'dwfrm_singleshipping_email_emailAddress': self.email,
                'dwfrm_singleshipping_shippingAddress_shippingMethodID': 'DHL-DE',
                'dwfrm_singleshipping_save': 'Continue to payment method',
                'dwfrm_singleshipping_securekey': securekey,
            }

            while True:
                try:
                    r = self.s.post(url, headers=self.headers, data=self.data, proxies=self.proxies)
                    if r.status_code == 200:
                        if r.text.split('<title>')[1].split('</title>')[0] == 'Checkout - pay':
                            try:
                                url = r.text.split('<form action="')[1].split('"')[0]
                                securekey = r.text.split('<input type="hidden" name="dwfrm_billing_securekey" value="')[1].split('"')[0]
                                securetoken = r.text.split('merchantToken&quot;:&quot;')[1].split('&')[0].strip()
                                break
                            except:
                                s_print(self.red(message='Failed To Submit Shipping - Retrying...'))
                                time.sleep(self.delay)
                        else:
                            s_print(self.red(message='Failed To Submit Shipping - Retrying...'))
                            time.sleep(self.delay)
                    elif r.status_code == 429:
                        s_print(self.red(message='Submit Shipping: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 403:
                        s_print(self.red(message='Submit Shipping: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 404:
                        s_print(self.red(message='Submit Shipping: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Submit Shipping: Error [{str(r.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)
                    continue

            self.headers = {
                'Host': 'www.arvato-payment.de',
                'sec-ch-ua': self.secChUa,
                'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'User-Agent': self.userAgent,
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.arvato-payment.de/Birkenstock-Adyen/Pmg.Site/WidgetApi/Home/Index?request={%22clientDomain%22:%22https://www.birkenstock.com%22,%22tokenizationServiceUrl%22:%22https://www.arvato-payment.de/Birkenstock-Adyen/Pmg.Site/WidgetApi/Home/Index%22,%22securityToken%22:%2207bf49cd-8e96-4bd2-af71-a2cf7680e11b%22,%22placeHolder%22:%22payNextWidgetContent_PAYPAL%22,%22countryCode%22:%22DE%22,%22currencyCode%22:%22EUR%22,%22culture%22:%22en-DE%22,%22cssUrl%22:%22https://www.birkenstock.com/on/demandware.static/Sites-DE-Site/-/en_DE/v1672986612435/css/paynext.css%22,%22mandateReference%22:%22%22,%22mandateConfirmationText%22:%22%22,%22firstName%22:%22%22,%22lastName%22:%22%22,%22showCvcHint%22:false,%22displayPaymentMethodsLogo%22:false,%22displayValidationErrors%22:false,%22busyIndicator%22:true,%22paymentMethods%22:%22PayPal%22,%22timeOut%22:0,%22amount%22:0,%22clearFrameAfterSuccessfulPayment%22:true,%22renderSuccessCallback%22:%22%22,%22inPageFrameId%22:%22ArvatoPayNextWidgetApi_payNextWidgetContent_PAYPAL%22,%22frameHeight%22:%221%22,%22frameWidth%22:%221%22,%22onWidgetContentResized%22:null,%22automaticParentResize%22:false,%22sendResizeNotification%22:false,%22disableIntroductionText%22:false,%22widgetFrameTitle%22:%22%22,%22extraData%22:%22%22,%22shippingAddress%22:{},%22orderItems%22:{}}',
                'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            self.params = {
                'callback': 'jQuery35103284109753818325_1673036270638',
                'SecurityToken': securetoken,
                'PaymentMethodName': '/SavePaymentDataPayPal',
                'EncryptedString': '&gMUKJW21dOJQjiwRYwjjgyq9BOfNnUgJUtDtTSp2hKssqKNPP63rNrHM8ZZh+ua2\nL1GIKoJkjhdLRjLMPYGLx6BGAkRY/b94lBWVn0wQvhNEQv2yLkp/ejgEZoCTwH36\npq9fWGTmhIYRQZRdWxTX0QnENaZQaOekPA36AQiegFblMSeTVFKasKmINd/vHD37\nHRr3AodPCRe925tSGXybE+pFIAQt1hpuVz9T3W9/1xurAIUg5w5fzOaqWuuFHz9n\nN8mG0+gnfHjYCAQdEVpw2HfET+lm5IUM3azIlgS+jJtJcd0UhCOckuozDccJWhg/\nXzSbslF0XKdWwtxBwsinPFSC7nwIxOL0y3AIFTYt+KrZ6Dl+zgdWl6HYdgxrJrlp\nksRvyJib4Umot0Ct5O6TdO6jsBs0uGYN7VXj7xWzJ77PDsVW/VAP6TF3YmRqhIq4\n1SbyylIvMMA39JxBWld8xDgqSimWo/QT9gcFG6ORccEHuoCXhGMCvTVU8qHDpg1g\n6S26WyTay8BTRMWBf/EuW/7rNaXWLYDLJO0+PM9z/4CTfQnsFXgk+TiH/ls80iWX\n74fHmTjynQFMcdvR6IvSSlWEknhdb7p2QbIV7kTBgg2v+XWngSjzVkJD114YlbSJ\n4znjj5hzJgHuHxEEP1KnwCZATdrt+Ykmjh+tT7TwrEc=\n&ZohXzFKeJlg1Ai38DpJ3DwDTexpIwqKrENLzdtvg5f3FxZ0FeAJYy5ZTf0tEyvax\nVxpoW2NrMdKG0XnGEk1UeOgGQ2erYawruioU1ISgKQSwceVDUemf+ll6JJa+AgtU\nHo0XcRE7+DEbmGo1Wd9KwdYJVBVOUuUonUDwFbA/9MRapwqiqgid6oRTSYpGbaN1\n4KYURC3kgkZ4poJ0y8XIu8wlUGCy8JMq4fbHLuHx/s0RlnVxvOeOaD9ZKfGoH8ef\nicvZk0kpIFLNvad4edRLcAMM4vrWnf298SkNLpEYiqxpe6upLXHczuhyWAmNfPft\nOQyeoNHWGlT/HadBPEXPcMRlXWpOjK1hQuJYUT8w4CyaHsrZZHxq8FUk8ZgBRZrQ\nlLSEuTHjHg27DA/EQFinQwxik/ZBLc/x16uFdzRMfrWkXp27yGOhVGGCFgE1dB5S\nr1L1evhBwiu15p78F62XwatH9+j9mfQjVJoWJlsii6Tbd/aBB3X/DV8cTuzAbgGz\num0gCEvPUx0g7zyvZ5wDKNbiiYZtYT/yt5da8AmqwFYLMLIxJSXlk53FPhMDZybN\ncSjtdH0Ujo6o6/HRF3SDrQz2NXBdZ3XScn9oTzfNMYou2g2p6onDf7vjQLXKwDbm\nWLMkXrcm1WC5zylxYTCg4LC9bI8Aj4fLbBvo4oXToiE=\n',
                '_': '1672996076254',
            }

            while True:
                try:
                    res = self.s.get('https://www.arvato-payment.de/Birkenstock-Adyen/Pmg.Site/V21/JsonPaymentService/SaveEncryptedData', headers=self.headers, params=self.params, proxies=self.proxies)
                    if res.status_code == 200:
                        try:
                            token = res.text.split('PaymentToken":"')[1].split('"')[0]
                            break
                        except:
                            s_print(self.red(message='Failed To Submit Payment [1] - Retrying...'))
                            time.sleep(self.delay)
                            continue
                    elif res.status_code == 429:
                        s_print(self.red(message='Submit Payment [1]: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif res.status_code == 403:
                        s_print(self.red(message='Submit Payment [1]: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif res.status_code == 404:
                        s_print(self.red(message='Submit Payment [1]: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Submit Payment [1]: Error [{str(res.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)
                    continue

            self.headers = {
                'Host': 'www.birkenstock.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': self.secChUa,
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'origin': 'https://www.birkenstock.com',
                'user-agent': self.userAgent,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': url,
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            self.data = {
                'dwfrm_billing_securekey': securekey,
                'dwfrm_billing_paymentToken': token,
                'dwfrm_billing_paymentCvn': '',
                'dwfrm_billing_paymentMethods_invoice_birthday_date': '',
                'dwfrm_billing_paymentMethods_invoice_birthday_month': '',
                'dwfrm_billing_paymentMethods_invoice_birthday_year': '',
                'dwfrm_billing_paymentMethods_selectedPaymentMethodID': 'PAYPAL',
                'dwfrm_billing_paymentMethods_creditCard_number': '',
                'dwfrm_billing_paymentMethods_creditCard_expiration_month': '',
                'dwfrm_billing_paymentMethods_creditCard_expiration_year': '',
                'dwfrm_billing_paymentMethods_creditCard_cvn': '',
                'dwfrm_billing_paymentMethods_creditCard_owner': '',
                'dwfrm_billing_paymentMethods_creditCard_encrypteddata': '',
                'dwfrm_adyPaydata_adyenFingerprint': 'DpqwU4zEdN0050000000000000KZbIQj6kzs0050271576cVB94iKzBGqBirNZgEUXBix7RX3az8002w7hYyfhAaY00000qZkTE00000nWGGLjCETHEC4FlSABmQ:40',
                'dwfrm_billing_save': [
                    'Continue to overview',
                    'Continue to overview',
                ],
            }

            while True:
                try:
                    r = self.s.post(url, headers=self.headers, data=self.data, proxies=self.proxies)
                    if r.status_code == 200:
                        if r.text.split('<title>')[1].split('</title>')[0] == 'Checkout - review order':
                            try:
                                self.orderUrl = r.text.split('<form action="')[1].split('"')[0]
                                self.securekey = r.text.split('<input type="hidden" name="dwfrm_summary_securekey" value="')[1].split('"')[0]
                                self.last = r.url
                                break
                            except:
                                s_print(self.red(message='Failed To Submit Payment [2] - Retrying...'))
                                time.sleep(self.delay)
                        else:
                            s_print(self.red(message='Failed To Submit Payment [2] - Retrying...'))
                            time.sleep(self.delay)
                    elif r.status_code == 429:
                        s_print(self.red(message='Submit Payment [2]: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 403:
                        s_print(self.red(message='Submit Payment [2]: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 404:
                        s_print(self.red(message='Submit Payment [2]: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Submit Payment [2]: Error [{str(r.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)
                    continue

        else:

            s_print(self.yellow(message='Getting Product...'))

            self.headers = {
                'Host': 'www.birkenstock.com',
                'sec-ch-ua': self.secChUa,
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': self.userAgent,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            self.params = {
                'pid': self.html,
                f'dwvar_{self.html}_color': self.color,
                f'dwvar_{self.color}_width': 'N',
                'groupSize': 'null',
                'Quantity': '1',
                'format': 'ajax',
            }

            while True:
                try:
                    r = self.s.get('https://www.birkenstock.com/on/demandware.store/Sites-DE-Site/en_DE/Product-Variation', headers=self.headers, params=self.params, proxies=self.proxies)
                    if r.status_code == 200:
                        sizes = re.findall('(?<=<li class="selectable " data-region="EU">)[^>]+',r.text)
                        if sizes == []:
                            s_print(self.yellow(message='Monitoring...'))
                            time.sleep(self.delay)
                        else:
                            break
                    elif r.status_code == 429:
                        s_print(self.red(message='Get Cart: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 403:
                        s_print(self.red(message='Get Cart: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 404:
                        s_print(self.red(message='Get Cart: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Get Cart: Error [{str(r.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)
                    continue

            s_print(self.yellow(message='Submitting Order...'))

            self.headers = {
                'Host': 'www.birkenstock.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': self.secChUa,
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'origin': 'https://www.birkenstock.com',
                'user-agent': self.userAgent,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': self.last,
                'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            }

            self.data = {
                'minicartPid': self.pid,
                'currency': 'EUR',
                'dwfrm_summary_currentDevice': 'DevL',
                'dwfrm_summary_acceptterms': 'true',
                'dwfrm_summary_save': 'Submit Order',
                'dwfrm_summary_securekey': self.securekey,
            }

            while True:
                try:
                    r = self.s.post(self.orderUrl, headers=self.headers, data=self.data, proxies=self.proxies, allow_redirects=False)
                    if r.status_code == 302:
                        try:
                            if r.text.split('<title>')[1].split('</title>')[0] == 'Redirect to payment provider':
                                s_print(self.green(message='Successful Checkout: ' + r.headers['Location']))
                                incSuccess()
                                webhook = DiscordWebhook(url=self.webhook, avatar_url='https://famousfoxes.com/hd/861.png', username="AlexAIO")
                                embed = DiscordEmbed(title=f":flushed: Complete Payment :flushed:", url=r.headers['Location'], color=0x023F85)
                                embed.add_embed_field(name="Store", value="Birkenstock")
                                embed.add_embed_field(name="Product", value=self.name)
                                embed.add_embed_field(name="Size", value=self.size)
                                embed.add_embed_field(name="Price", value=self.price)
                                embed.add_embed_field(name="Payment Method", value="PayPal")
                                if self.discount != '':
                                    embed.add_embed_field(name="Discount Code", value=self.discount)
                                embed.set_thumbnail(url=self.image)
                                embed.set_footer(icon_url='https://famousfoxes.com/hd/861.png', text='by AlexW#9999')
                                embed.set_timestamp()
                                webhook.add_embed(embed)
                                webhook.execute()
                                break
                            else:
                                s_print(self.red(message='Failed Checkout'))
                                break
                        except:
                            s_print(self.red(message='Failed Checkout'))
                            break
                    elif r.status_code == 429:
                        s_print(self.red(message='Submit Order: Rate Limited [429] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 403:
                        s_print(self.red(message='Submit Order: Proxy Banned [403] - Retrying...'))
                        time.sleep(self.delay)
                    elif r.status_code == 404:
                        s_print(self.red(message='Submit Order: Not Found [404] - Retrying...'))
                        time.sleep(self.delay)
                    else:
                        s_print(self.red(message=f'Submit Order: Error [{str(r.status_code)}] - Retrying...'))
                        time.sleep(self.delay)
                except ProxyError:
                    s_print(self.red(message='Proxy Error - Retrying...'))
                    time.sleep(self.delay)
                    continue
                except Exception as e:
                    s_print(self.red(message=f'Request Failed - {type(e).__name__}'))
                    time.sleep(self.delay)
                    continue