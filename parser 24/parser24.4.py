import requests
from bs4 import BeautifulSoup
import csv


def parseMag():
    r = requests.get(url='https://retrymaster.github.io/1234.html')
    soup = BeautifulSoup(r.text, 'lxml')
    data = []

    cards = soup.find_all('a', class_='card-sale_catalogue')
    for card in cards:
        card_title = card.find('div', class_='card-sale__title').text.strip()
        card_price_integer = card.find('div', class_='label__price_new').find('span', class_='label__price-integer').text.strip()
        card_price_decimal = card.find('div', class_='label__price_new').find('span',class_='label__price-decimal').text.strip()
        card_price = f'{card_price_integer}.{card_price_decimal}'
        data.append([card_title, card_price])
        with open('info.csv', 'w') as file:
            writer = csv.writer(file)

            writer.writerow(
                ['Название товара:', 'Цена по акции:']
            )
            writer.writerows(
                data
            )
            print('готово')

if __name__ == '__main__':
    parseMag()