import requests, bs4


# res = requests.get("https://www.vultr.com/products/cloud-compute/#pricing")

res = requests.get("https://www.vultr.com/pricing/#cloud-compute/")
# print(type(res))
# print(res.status_code)
# print("len:", len(res.text))
# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'html5lib')
cloud = soup.select('#cloud-compute')[0]
table = cloud.find_all("div", attrs={"class": "pt__row"})
# print(table)

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
        # print(cell)  # <div class="pt__cell js-price"><strong>4.00</strong> TB<span class="is-hidden-lg-up"> Bandwidth</span></div>
        cell_info = str(str(cell).split('<strong>')[1]).split('</strong>')
        valor = cell_info[0]
        unidade = cell_info[1].split('<')[0]
        tipo +=1
        if tipo != 6:
            cell_info = [tipos.get(str(tipo)), valor + str(unidade).removeprefix("\xa0")]
            row_info[cell_info[0]] = cell_info[1]
    table_info.append(row_info)
    print(row_info)
