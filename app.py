import requests
from bs4 import BeautifulSoup

def fetch_page():
    url = "https://www.mercadolivre.com.br/macbook-pro-macbook-pro-14-m3-pro-14-space-black-18gb-de-ram-512gb-ssd-apple-m3/p/MLB28766778#polycard_client=search-nordic&searchVariation=MLB28766778&wid=MLB5065017432&position=4&search_layout=grid&type=product&tracking_id=f4539774-3f30-4a51-93c9-c8c5caa7c302&sid=search"
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_= 'ui-pdp-title').get_text()
    prices = soup.find_all('span', class_ = 'andes-money-amount__fraction')
    old_price : int = int(prices[0].get_text().replace('.',''))
    new_price : int = int(prices[1].get_text().replace('.',''))
    installment_price : int = int(prices[2].get_text().replace('.',''))
    #print(f"Product Name: {product_name}")
    #print(f"Product Price: {prices[0].get_text()}")
    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price
    }

if __name__ == "__main__":
    page_content = fetch_page()
    produto_value = parse_page(page_content)

    print(produto_value)