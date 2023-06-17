# BirkenstockAIO
This is a simple requests based bot for the website https://www.birkenstock.com/ written in Python. It is designed to be able to get your hands on limited or just sold out shoes in any form with a variety of helpful modules.
The main intention are educational purposes for anyone interested in such software and how it is structured.  

**Features**
* Checkout module with PID support only and PayPal as payment method
* Discount generator with the help of Selenium for a rarily used captcha
* Product scraper to scrape various info from a product including size PIDs
* Use of imap module to retrieve verify links and discount straight from your gmail
* Use of databases to save your checkouts and scraped products
* Use of discord webhooks to beautifully display checkouts
* Multi threading by task creation through CSV file tasks.csv
* Optional proxy support (empty for localhost usage)
* Both catchall and gmail with dot trick supported

## Setup
1. Clone the repository or download the .zip version.
2. Navigate to the folder and run this command to download all necessary modules:
```
pip install -r requirements.txt
```
3. Fill your information into tasks.csv and config.json files to start running.

## Notes
Make sure to use real info for your tasks to be able to test. Otherwise it will result in a shipping error.
Information on imap you can find here for example: https://hotter.io/docs/email-accounts/app-password-gmail/
If you get a chromedriver exception, make sure to redownload chromedriver matching your actual version in your browser.
