import pandas as pd
from scrap import scrap

def star_ch():
    url = 'https://bk.tw.lvfukeji.com/wiki/%E6%98%9F%E5%BA%A7%E5%88%97%E8%A1%A8'
    soup = scrap(url)
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
    df.bs = df.bs.apply(lambda x: x.strip('\n'))
    df1 = df.bs.str.extract(r'(?P<bs_name_bayer>.*)\((?P<bs_name_cn>.*)\)')
    df_ch = pd.merge(df, df1, on='name')
    return df_ch


