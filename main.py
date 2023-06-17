from colorama import Fore
from datetime import datetime
import os
import json
import asyncio
from threading import Lock, Thread
import csv
from colored import fg, attr

version = '0.0.1'

try:
    with open('tasks.csv') as csvfile:
        pass
    csvfile.close()
except FileNotFoundError:
    with open('tasks.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['PID', 'Email', 'First Name', 'Last Name', 'Street', 'House Number', 'Phone', 'Post Code', 'City', 'State', 'Discount', 'Delay', 'Webhook'])
    csvfile.close()

try:
    with open('proxies.txt', 'r') as proxfile:
        proxfile.close()
except:
    with open('proxies.txt', 'w') as proxfile:
        proxfile.close()

try:
    with open('config.json', 'r') as config_json:
        data = json.loads(config_json.read())
        config_json.close()
except FileNotFoundError:
    with open('config.json', 'w') as config:
        data = {
            "imap_mail": "",
            "imap_password": "",
            "catchall": "",
        }
        json.dump(data, config)
    config.close()

print('''  ____  _      _                  _             _              _____ ____  
 |  _ \(_)    | |                | |           | |       /\   |_   _/ __ \ 
 | |_) |_ _ __| | _____ _ __  ___| |_ ___   ___| | __   /  \    | || |  | |
 |  _ <| | '__| |/ / _ \ '_ \/ __| __/ _ \ / __| |/ /  / /\ \   | || |  | |
 | |_) | | |  |   <  __/ | | \__ \ || (_) | (__|   <  / ____ \ _| || |__| |
 |____/|_|_|  |_|\_\___|_| |_|___/\__\___/ \___|_|\_\/_/    \_\_____\____/ 
                                                                           
                                                                           ''')

print("%s  Welcome to BirkenstockAIO v" % (fg('cyan'))+version+"!%s\n" % (attr('reset')))
print("%s  [1] - Checkout Module%s" % (fg('yellow'), attr('reset')))
print("%s  [2] - Discount Generator%s" % (fg('yellow'), attr('reset')))
def select():
    while(1):
        option = input("%s  Please select a module: %s" % (fg('yellow'), attr('reset')))
        try:
            option = int(option)
            if option in [1,2]:
                break
            else:
                print(f"%s  {str(option)} is not a valid option. Try again with a number from 1 to 2.%s" % (fg('red'), attr('reset')))
        except Exception as e:
            print(e)
            print(("%s  Invalid input! Try again:%s" % (fg('red'), attr('reset'))))
    clear = lambda: os.system('cls')
    clear()
    if option == 1:
        import birkenstock
        try:
            with open('tasks.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                i = 0

                for row in csv_reader:
                    pid = row['PID']
                    email = row['Email']
                    fname = row['First Name']
                    lname = row['Last Name']
                    address = row['Street']
                    number = row['House Number']
                    phone = row['Phone']
                    postcode = row['Post Code']
                    city = row['City']
                    region = row['State']
                    discount = row['Discount']
                    delay = row['Delay']
                    webhook = row['Webhook']
                    i += 1

                    t = Thread(target=birkenstock.Birkenstock, args=(pid, email, fname, lname, address, number, phone, postcode, city, region, discount, delay, webhook, i))
                    t.start()
        except Exception as e:
            print(e)
            print(("%sFailed reading tasks!%s" % (fg('red'), attr('reset'))))
    elif option == 2:
        import birkenstocknewsletter
        amount = input("%sPlease enter your desired tasks amount: %s" % (fg('yellow'), attr('reset')))
        clear = lambda: os.system('cls')
        clear()
        for i in range(int(amount)):
            t = Thread(target=birkenstocknewsletter.Birkenstock, args=(i+1,))
            t.start()
select()