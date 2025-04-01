import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import sqlite3

def fetch_page():
    url = "https://www.mercadolivre.com.br/macbook-pro-macbook-pro-14-m3-pro-14-space-black-18gb-de-ram-512gb-ssd-apple-m3/p/MLB28766778#polycard_client=search-nordic&searchVariation=MLB28766778&wid=MLB5065017432&position=4&search_layout=grid&type=product&tracking_id=f4539774-3f30-4a51-93c9-c8c5caa7c302&sid=search"
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_= 'ui-pdp-title').get_text()
    prices = soup.find_all('span', class_ = 'andes-money-amount__fraction')
    old_price : int = int(prices[0].get_text().replace('.',''))
    installment_price : int = int(prices[2].get_text().replace('.',''))
    #print(f"Product Name: {product_name}")
    #print(f"Product Price: {prices[0].get_text()}")

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    return {
        'product_name': product_name,
        'old_price': old_price,
        'installment_price': installment_price,
        'timestamp': timestamp
    }

def create_conection(db_name = "macbook_price.db"):
    """Cria uma conexão com o banco de dados SQlite. """
    conn = sqlite3.connect(db_name)
    return conn

def setup_db(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            old_price REAL,
            installment_price REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    

def db_save(conn, produto_value):
    new_row = pd.DataFrame([produto_value])
    new_row.to_sql('prices', conn, if_exists='append', index=False)

if __name__ == "__main__":

    conn = create_conection()
    setup_db(conn)

    while True:
        page_content = fetch_page()
        produto_value = parse_page(page_content)
        db_save(conn, produto_value)
        print(f"Dados salvos com sucesso: {produto_value}")
        time.sleep(10)

        