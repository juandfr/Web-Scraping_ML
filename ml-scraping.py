import requests
from bs4 import BeautifulSoup

base_url = 'https://lista.mercadolivre.com.br/'

product_name = input('Nome do produto:')

response = requests.get(base_url + product_name)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for product in products:
    title = product.find('h2', attrs={'class': 'ui-search-item__title'})
    link = product.find('a', attrs={'class': 'ui-search-link'})

    real_price = product.find('span', attrs={'class': 'price-tag-fraction'})
    cents_price = product.find('span', attrs={'class': 'price-tag-cents'})

    print(product.prettify())
    print('Título do produto:', title.text)
    print('Link do produto:', link['href'])

    if (cents_price):
        print('Preço do produto: R$', real_price.text + ',' + cents_price.text)
    else:
        print('Preço do produto: R$', real_price.text)
    
    print('\n\n')
    break


