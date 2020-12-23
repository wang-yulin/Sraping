import pandas as pd 
from bs4 import BeautifulSoup
import requests

url = 'https://bk.tw.lvfukeji.com/wiki/%E6%98%9F%E5%BA%A7%E5%88%97%E8%A1%A8'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url=url, headers=headers)
payload = response.content

soup = BeautifulSoup(payload, "html.parser")
table = soup.find("table", class_='wikitable sortable')
column_names = [th.text for th in table.tbody.tr.find_all('th')]

rows = []
for tr in table.tbody.find_all('tr')[1:]:
    row = []
    for td in tr.find_all('td'):
        row.append(td.text)
    rows.append(row)

df = pd.DataFrame(rows, columns=column_names)
df.columns = ['name_cn', 'abbr', 'name', 'area', 'ra', 'dec', 'quadrant', 'family', 'bs']
df.set_index('name', inplace=True)

df1 = pd.merge(df, df.bs.str.extract(r'(?P<bs_name_bayer>.*)\((?P<bs_name_cn>.*)\)'), on='name')
