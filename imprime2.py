# imprime2.py
# go horse script gambiarra do archive

import requests, bs4, re, sys, json
import pandas as pd


# opções: --print, --save_csv, --save_json
try:
    option = sys.argv[1]
except IndexError:
    print("Please, run again with an option: ",
          "--print, --save_json or --save_csv")
    sys.exit(0)
else:
    if option not in ["--print", "--save_json", "--save_csv"]:
        print(f"This {option} is not valid, try again with an option: ",
              "--print, --save_json or --save_csv")
        sys.exit(0)


## 2 páginas-alvo:
# A quarta etapa exige que você extraia as informações também da
# página-alvo 2, tendo as mesmas funcionalidades da etapa anterior.

resp = requests.get("https://web.archive.org/web/20210131084315/https://www.digitalocean.com/pricing/")
info = "table"
soup = bs4.BeautifulSoup(resp.text, 'html5lib')
tables = soup.select(info)
table = soup.find_all("tbody")
titulos = ['MEMORY', 'VCPU', 'BANDWIDTH', 'STORAGE', 'PRICE']
table_info = []

n = 0
for rows in table[0]:
    n +=1
    row = re.findall(r'<td>(.\w+)</td>', str(rows), re.I)
    price = re.findall(r'<td data-price="(.[\d]+)', str(rows), re.I)[0]
    row.append(price)
    table_info.append(row)

df = pd.DataFrame(table_info, columns=titulos)
print(df)

if option == "--print":
    sys.exit(0)

df.to_json('prices2.json')

if option == "--save_json":
    sys.exit(0)

df.to_csv("prices2.csv", sep=';')

# TODO:

# refatorar (-> funções)

# testes

# type hint e/ou docstrings nas funções

