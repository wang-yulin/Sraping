from scrap import scrap
import pandas as pd
import numpy as np

def links():
    BASE_URL = 'https://www.lcsd.gov.hk/CE/Museum/Space/zh_CN/web/spm/starshine/resources/constemyth/'
    url_bs = 'https://www.lcsd.gov.hk/CE/Museum/Space/zh_CN/web/spm/starshine/resources/constemyth/chinengstars.html'
    soup = scrap(url_bs)
    page_address = soup.find('div', class_="pagination").find_all('a')

    links = []
    for link in page_address:
        page = BASE_URL + link['href']
        links.append(page)
    return links

def star_bs():
    rows = []
    for link in links():
        soup = scrap(link)
        tables = soup.find_all('table', class_='table_space')
        for table in tables:
            for tr in table.tbody.find_all('tr')[1:]:
                row = []
                for td in tr.find_all('td'):
                    row.append(td.text)
                rows.append(row)

    column_names = ['name_en', 'num', 'name', 'name_cn', 'ra', 'other']
    df = pd.DataFrame(data=rows, columns=column_names)

    df['top20'] = np.where(df['name_with_suffix'].str.endswith('**'), 'yes', 'no')
    df['commonly_used'] = np.where(df['name_with_suffix'].str.endswith('*'), 'yes', 'no')
    df['name'] = [s.split(r' *', 1)[0].strip() for s in df['name_with_suffix']]
    df['name_cn'] = [s.replace(' ', '') for s in df['name_cn']]

    df.to_csv('assets/stars.csv')

if "__name__" == "__main__":
    star_bs()