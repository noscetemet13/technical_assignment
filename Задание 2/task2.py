import requests
import pandas
import time
import re

url = 'https://www.goszakup.gov.kz/ru/registry/rqc?count_record=50&page='
urls, info = [], {}

# Create all possible urls of members
for page in range(1, 11):
    mainResponse = requests.get(url + str(page))
    memberURLs = re.findall(
        r'https:\/\/www\.goszakup\.gov\.kz\/ru\/registry\/show_supplier\/\d+',
        mainResponse.text)
    # print(f'{page}th page: {memberURLs}')
    urls += memberURLs

# Parsing data from urls
for link in urls:
    response = requests.get(link).text
    memberNAME = re.search(r'<h1>(.+)<', response)
    BIN = re.search(r'БИН.+\n.+<td>(\d+)', response)
    bossNAME = re.search(r'ФИО.+\n.+<td>(.+)<', response)
    bossIIN = re.search(r'ИИН.+\n.+<td>(\d+)', response)
    addresses = re.findall(r'\W{34}(.+)\W{28}<\/td>\n.+\n.+.+адрес', response)

    memberNAME = memberNAME.group(1) if memberNAME else 'None'
    BIN = BIN.group(1) if BIN else 'None'
    bossNAME = bossNAME.group(1) if bossNAME else 'None'
    bossIIN = bossIIN.group(1) if bossIIN else 'None'

    if not memberNAME in info: info[memberNAME] = [BIN, bossNAME, bossIIN, addresses]
    time.sleep(1)

# Create excel sheet
worksheet = {
    'Наименование организации': [],
    'БИН организации': [],
    'ФИО руководителя': [],
    'ИИН руководителя': [],
    'Полный адрес организации': []
}

# Input data from info to worksheet
for key, value in info.items():
    worksheet['Наименование организации'].append(key)
    worksheet['БИН организации'].append(value[0])
    worksheet['ФИО руководителя'].append(value[1])
    worksheet['ИИН руководителя'].append(value[2])
    worksheet['Полный адрес организации'].append('. '.join(value[3]))

# Create excel file
df = pandas.DataFrame(worksheet)
with pandas.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, index=False)