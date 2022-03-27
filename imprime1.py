# imprime1.py
# Teste backend

import requests, bs4, re, json, sys
from urllib.parse import urlparse
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


# simplest link crawler
url1 = "https://www.vultr.com/products/cloud-compute/#pricing"
subject1 = "cloud-compute"

def crawler(url, subject):
    parsed_url = urlparse(url)
    resp = requests.get(url)
    for i in re.findall(
            "<a[^>]+href=\"(.*?)\"[^>]*>(.*)?</a>", resp.text, re.I
            ):
        link = i[0]
        if subject in link:
            slink = "https://" + str(parsed_url.netloc + link)
            try:
                res = requests.get(slink)
                break
            except:
                continue
    return res


res = crawler(url1, subject1)

## 1 página-alvo, imprime na tela:
# A primeira etapa exige que o seu crawler funcione para a página alvo 1,
# capturando as informações e sendo capaz de imprimi-las na linha de comando
# em formato arbitrário.

apenas = "#cloud-compute"

tipos = {
        '1': 'VCPU',
        '2': 'MEMORY',
        '3': 'BANDWIDTH',
        '4': 'STORAGE',
        '5': 'PRICE'
        }

def catcher(response_text, info, specs):
    soup = bs4.BeautifulSoup(response_text, 'html5lib')
    cloud = soup.select(info)[0]
    table = cloud.find_all("div", attrs={"class": "pt__row"})
    table_info = []
    for row in table:
        cells = row.find_all("div", attrs={"class": "pt__cell"})
        tipo = 0
        row_info = dict()
        for cell in cells:
            cell_info = str(str(cell).split('<strong>')[1]).split('</strong>')
            valor = cell_info[0]
            unidade = cell_info[1].split('<')[0]
            tipo +=1
            if tipo != 6:
                cell_info = [
                        specs.get(str(tipo)),
                        valor + str(unidade).removeprefix("\xa0")
                        ]
                row_info[cell_info[0]] = cell_info[1]
        table_info.append(row_info)

    return pd.DataFrame.from_dict(table_info), table_info


df, dict_t = catcher(res.text, apenas, tipos)

print(df)

if option == "--print":
    sys.exit(0)

## 1 página-alvo, imprime na tela, salva em json:
# A segunda etapa exige que o seu crawler funcione para a mesma página-alvo
# da etapa anterior, tendo as mesmas funcionalidades da etapa anterior,
# mas também sendo capaz de salvar os dados em um arquivo em formato json.


with open('prices.json', 'w') as out_file:
    json.dump(dict_t, out_file, indent = 4)

if option == "--save_json":
    sys.exit(0)

## 1 página-alvo, imprime na tela, salva em json, salva em csv:
# A terceira etapa exige que o seu crawler funcione para a mesma página-alvo
# da etapa anterior, tendo as mesmas funcionalidades da etapa anterior,
# mas também sendo capaz de salvar os dados em um arquivo em formato csv.

df.to_csv("prices.csv", sep=';')


## SPECIFICATIONS: ##

# Páginas-alvo:

# 1. https://www.vultr.com/products/cloud-compute/#pricing
# (apenas SSD Cloud Instances)

# 2. https://www.digitalocean.com/pricing/ (apenas tabela Basic droplets)

#####################

# TODO:

# testes

# type hint e/ou docstrings nas funções

