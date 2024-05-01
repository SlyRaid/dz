import datetime
import requests
from bs4 import BeautifulSoup as Bs
import csv

url = 'https://coinmarketcap.com/'
response = requests.get(url).text
soup = Bs(response, 'html.parser')
tr = soup.find_all('tr', style="cursor:pointer")
all_names = []
markcaps = []
markcaps_int = []
for i in tr:
    name = i.find('p', {'class': 'sc-4984dd93-0 kKpPOn'}).text
    market_cap = i.find('span', {'class': 'sc-7bc56c81-1 bCdPBp'}).text
    all_names.append(name)
    markcaps.append(market_cap[1:])
    markcaps_int.append(int(market_cap[1:].replace(',', '')))

# data_file_name = datetime.datetime.now().strftime("%H.%M %d.%m.%Y") + '.csv'
# with open(data_file_name, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file, delimiter=' ')
#     writer.writerow(['Name', 'MC', 'MP'])
#     count = 0
#     for row in range(len(all_names)):
#         writer.writerow([all_names[count], markcaps[count], f'{round(markcaps_int[count] / sum(markcaps_int) * 100)}%'])
#         count += 1
count = 0
for row in range(len(all_names)):
    print(count + 1, [all_names[count], markcaps[count], f'{round(markcaps_int[count] / sum(markcaps_int) * 100)}%'])
    count += 1
