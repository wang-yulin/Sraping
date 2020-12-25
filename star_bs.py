from scrap import scrap
import pandas as pd

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
    tables = []
    for link in links():
        soup = scrap(link)
        table = soup.find('table', class_='table_space')
        tables.append(table)

    rows = []
    for table in tables:
        if table:
            for tr in table.tbody.find_all('tr')[1:]:
                row = []
                for td in tr.find_all('td'):
                    row.append(td.text)
                rows.append(row)

    column_names = ['name_en', 'num', 'name', 'name_cn', 'ra', 'other']
    df_bs = pd.DataFrame(data=rows, columns=column_names)

    return df_bs

if "__name__" == "__main__":
    star_bs()