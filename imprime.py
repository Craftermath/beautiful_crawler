# imprime.py
# Teste backend

import requests, bs4, re
from urllib.parse import urlparse


## 1 página-alvo, imprime na tela:
# A primeira etapa exige que o seu crawler funcione para a página alvo 1,
# capturando as informações e sendo capaz de imprimi-las na linha de comando
# em formato arbitrário.

# simplest link crawler
spec_url = "https://www.vultr.com/products/cloud-compute/#pricing"
parsed_url = urlparse(spec_url)
resp = requests.get(spec_url)
for i in re.findall("<a[^>]+href=\"(.*?)\"[^>]*>(.*)?</a>", resp.text, re.I):
    link = i[0]
    if "cloud-compute" in link:
        slink = "https://" + str(parsed_url.netloc + link)
        try:
            res = requests.get(slink)
            break
        except:
            continue

# info scraping
soup = bs4.BeautifulSoup(res.text, 'html5lib')
cloud = soup.select('#cloud-compute')[0]
table = cloud.find_all("div", attrs={"class": "pt__row"})

tipos = {
        '1': 'VCPU',
        '2': 'MEMORY',
        '3': 'BANDWIDTH',
        '4': 'STORAGE',
        '5': 'PRICE'
        }

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
                    tipos.get(str(tipo)),
                    valor + str(unidade).removeprefix("\xa0")
                    ]
            row_info[cell_info[0]] = cell_info[1]
    table_info.append(row_info)
    print(row_info)

# "formato arbitrário" é um dicionário por linha da tabela por enquanto

# TODO:

## 1 página-alvo, imprime na tela, salva em json
# A segunda etapa exige que o seu crawler funcione para a mesma página-alvo da etapa
# anterior, tendo as mesmas funcionalidades da etapa anterior, mas também sendo capaz de
# salvar os dados em um arquivo em formato json.

## 1 página-alvo, imprime na tela, salva em json, salva em csv
# A terceira etapa exige que o seu crawler funcione para a mesma página-alvo da etapa
# anterior, tendo as mesmas funcionalidades da etapa anterior, mas também sendo capaz de
# salvar os dados em um arquivo em formato csv.

## 2 páginas-alvo
# A quarta etapa exige que você extraia as informações também da página-alvo 2, tendo as
# mesmas funcionalidades da etapa anterior.

