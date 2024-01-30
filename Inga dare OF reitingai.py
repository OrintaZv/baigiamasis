import requests
from bs4 import BeautifulSoup
import pandas as pd

baltictour_egzotine = []

def extract_data_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', class_='s2l-el special__offer')
    page_data = []

    for product in products:
        salis = product.find('div', class_='city').text.strip()
        regionas = product.find('div', class_='country').text.strip()
        trukme = product.find('div', class_='nights').text.strip().split(" ", 1)[0]
        kainaold = product.find('div', class_='price').text.strip().replace(' €', '').replace('nuo\n', '')
        reitingas = product.find('div', class_='stars')

        # Tikriname, ar rasta reitingo elementas
        if reitingas:
            # Jei taip, gausiu reitingo vertę (pvz., naudodami tekstą)
            reitingas = reitingas['class'][1].replace('stars-', '')
        else:
            # Jei ne, paliekame reitingą tuščią ar priskiriame kitą numatytąją vertę
            reitingas = 'Nera reitingo'

        data = product.find('div', class_='date').text.strip().split(" ", 1)[0]
        agentura = 'Baltictours'

        if len(kainaold) > 4:
            kainabeakcijos = kainaold[0:4]
            kaina = kainaold[4:8]
        else:
            kainabeakcijos = kainaold
            kaina = kainaold

        page_data.append({
            'Salis': salis,
            'Regionas': regionas,
            'Trukme': trukme,
            'Kaina': kaina,
            'Reitingas': reitingas,
            'Data': data,
            'Agentura': agentura,
            'Keliones tipas': "egzotine"
        })

    return page_data

base_url = 'https://www.baltictours.lt/kelioniu-kryptys/egzotines-keliones/?page='
all_data = []

for page_num in range(1, 6):  # Pavyzdžiui, peržiūrima 5 puslapiai (gali būti keičiamas)
    url = f'{base_url}{page_num}'
    data_from_page = extract_data_from_page(url)
    all_data.extend(data_from_page)

# Sukuriam DataFrame iš visų surinktų duomenų
df_all_data = pd.DataFrame(all_data)
df_all_data.to_csv('baltictour_egzotine_all_pages.csv', index=False)


#print(df_all_data[['Reitingas']])   veikia

#print("Reitingai:")
#print(df_all_data['Reitingas'])

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print("Kelionių informacija:")
print(df_all_data[['Salis', 'Regionas', 'Trukme', 'Kaina', 'Reitingas', 'Data', 'Agentura', 'Keliones tipas']])


