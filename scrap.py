from bs4 import BeautifulSoup
import requests

def scrap(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        payload = response.content
        soup = BeautifulSoup(payload, "html.parser")
        return soup


if __name__ == "__main__":
    url = 'https://www.baidu.com/'
    soup = scrap(url)
    soup