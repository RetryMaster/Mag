import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

def getPage(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'lxml')
    return s

def getCards(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'lxml')
    cards = s.find_all('a', class_='card-sale_catalogue')
    return cards

def init__driver():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    return driver

def lookup(driver, a):
    try:
        driver.get(a)
        time.sleep(3)
        count = 0
        while count<5:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            count+=1
            time.sleep(3)
            getCards(a)
        allinfo = getCards(a)
        print(getCards(a))
        return allinfo
    # except:
    #     return 0
    finally:
        driver.close()


a = 'https://magnit.ru/promo/?format[]=mm'
driver = init__driver()
parsedhtml = lookup(driver, a)
# with open(f'1ndex.html', 'w') as file:
#     file.write(parsedhtml)
print(parsedhtml, 'good luck')