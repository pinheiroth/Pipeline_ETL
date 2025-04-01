import requests

def fetch_page():
    url = "https://www.mercadolivre.com.br/macbook-pro-macbook-pro-14-m3-pro-14-space-black-18gb-de-ram-512gb-ssd-apple-m3/p/MLB28766778#polycard_client=search-nordic&searchVariation=MLB28766778&wid=MLB5065017432&position=4&search_layout=grid&type=product&tracking_id=f4539774-3f30-4a51-93c9-c8c5caa7c302&sid=search"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    page_content = fetch_page()
    print(page_content)