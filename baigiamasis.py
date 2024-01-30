import requests
from bs4 import BeautifulSoup
import pandas as pd

kelioniupanorama_egzotine = []
for i in range(0,2):
    if i == 0:
        target = "https://www.kelioniupanorama.lt/?types=4"
    else:
        target = f"https://www.kelioniupanorama.lt/{i}0?types=4"
    response = requests.get(target)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', class_='c-trip')
    for product in products:
        salis_regionas = product.find('div', class_='c-trip__description').find('p').text.strip().split(',')
        salis = salis_regionas[0].strip()
        regionas = salis_regionas[1].strip()
        data_trukme = product.find('div', class_='c-trip__info').text.strip().split()
        # print(data_trukme)
        if len(data_trukme) > 0:
            data = data_trukme[0].strip()
        else:
            data = "Nenurodyta"
        if len(data_trukme) > 1:
            trukme = data_trukme[1].strip()
        else:
            data = "Nenurodyta"
        kaina = product.find('div', class_='c-trip__price').text.strip().replace(' €', '')
        reitingas_count = product.find('div', class_='c-trip__tags').find('span')
        reitingas = str(reitingas_count).replace('<span><i class="icon-star-', "").replace('"></i></span>', '')
        agentura = 'Kelioniu panorama'
        # print(products)

        kelioniupanorama_egzotine.append({
            'Salis': salis,
            'Regionas': regionas,
            'Trukme': trukme,
            'Data': data,
            'Kaina': kaina,
            'Reitingas' : reitingas,
            'agentura': agentura,
            'Keliones tipas': "egzotine"
        })

dfkelioniupanorama_egzotine = pd.DataFrame(kelioniupanorama_egzotine)
dfkelioniupanorama_egzotine.to_csv('kelioniupanorama_egzotine.csv', index=False)

kelioniupanorama_pazintine=[]
target = f"https://www.kelioniupanorama.lt/?types=1"
response = requests.get(target)
soup = BeautifulSoup(response.content, 'html.parser')



products = soup.find_all('div', class_='c-trip')
for product in products:
    salis_regionas = product.find('div', class_='c-trip__description').find('p').text.strip().split(',')
    salis = salis_regionas[0].strip()
    regionas = salis_regionas[1].strip()
    data_trukme = product.find('div', class_='c-trip__info').text.strip().split()
    # print(data_trukme)
    if len(data_trukme) > 0:
        data = data_trukme[0].strip()
    else:
        data = "Nenurodyta"
    if len(data_trukme) > 1:
        trukme = data_trukme[1].strip()
    else:
        data = "Nenurodyta"
    kaina = product.find('div', class_='c-trip__price').text.strip().replace(' €','')
    reitingas_count = product.find('div', class_='c-trip__tags').find('span')
    reitingas = str(reitingas_count).replace('<span><i class="icon-star-', "").replace('"></i></span>', '')
    agentura = 'Kelioniu panorama'
    #print(products)

    kelioniupanorama_pazintine.append({
        'Salis' : salis,
        'Regionas' : regionas,
        'Trukme': trukme,
        'Data' : data,
        'Kaina' : kaina,
        'Reitingas' : reitingas,
        'agentura': agentura,
        'Keliones tipas' : "pazintine"
})


dfkelioniupanorama_pazintine = pd.DataFrame(kelioniupanorama_pazintine)
dfkelioniupanorama_pazintine.to_csv('kelioniupanorama_pazintine.csv', index=False)

kelioniupanorama_poilsine = []
for x in range(0, 58):
    if x == 0:
        target = "https://www.kelioniupanorama.lt/?types=2"
    else:
        target = f"https://www.kelioniupanorama.lt/{x}0?types=2"
    response = requests.get(target)
    #print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', class_='c-trip')
    for product in products:
        salis_regionas = product.find('div', class_='c-trip__description').find('p').text.strip().split(',')
        salis = salis_regionas[0].strip()
        regionas = salis_regionas[1].strip()
        data_trukme = product.find('div', class_='c-trip__info').text.strip().split()
        # print(data_trukme)
        if len(data_trukme) >= 1:
            if str(data_trukme[0]) == 'AI' or data_trukme[0] == "UAI" or data_trukme[0] == "BB" or data_trukme[
                0] == "RO" or data_trukme[0] == "HB":
                data = "Nenurodyta"
            else:
                data = data_trukme[0]
        if len(data_trukme) >= 1:
            if len(data_trukme[1]) >= 1:
                trukme = data_trukme[1].strip()
            else:
                trukme = "Nenurodyta"
        kaina = product.find('div', class_='c-trip__price').text.strip().replace(' €', '')
        reitingas_count = product.find('div', class_='c-trip__tags').find('span')
        reitingas = str(reitingas_count).replace('<span><i class="icon-star-', "").replace('"></i></span>', '')
        agentura = 'Kelioniu panorama'
        # print(products)

        kelioniupanorama_poilsine.append({
            'Salis': salis,
            'Regionas': regionas,
            'Trukme': trukme,
            'Data': data,
            'Kaina': kaina,
            'Reitingas' : reitingas,
            'agentura': agentura,
            'Keliones tipas': "poilsine"
        })

dfkelioniupanorama_poilsine = pd.DataFrame(kelioniupanorama_poilsine)
dfkelioniupanorama_poilsine.to_csv('kelioniupanorama_poilsine.csv', index=False)

dfbendraspanorama = pd.concat([dfkelioniupanorama_pazintine, dfkelioniupanorama_egzotine, dfkelioniupanorama_poilsine], axis=0)
dfbendraspanorama.to_csv('Bendraspanorama.csv', index=False)

baltictour_egzotine=[]
target = 'https://www.baltictours.lt/kelioniu-kryptys/egzotines-keliones/'
response = requests.get(target)
soup = BeautifulSoup(response.content,'html.parser')
# print(response.status_code)


products = soup.find_all('div', class_='s2l-el special__offer')
for product in products:
    salis = product.find('div', class_='city').text.strip()
    regionas = product.find('div', class_='country').text.strip()
    trukme = product.find('div', class_='nights').text.strip().split(" ", 1)[0]
    kaina = product.find('div', class_='price').text.strip().replace('nuo\n','').split(" €")[0]
    reitingas_count = product.find('div', class_='stars')
    reitingas = str(reitingas_count).replace('<div class="stars stars-','').replace('"></div>','')
    data = product.find('div', class_='date').text.strip()[0:10]
    agentura = 'Baltictours'



    baltictour_egzotine.append({
        'Salis' : salis,
        'Regionas' : regionas,
        'Trukme' : trukme,
        'Kaina' : kaina,
        'Data' : data,
        # 'Kaina be Akcijos': kainabeakcijos,
        'Reitingas' : reitingas,
        'agentura' : agentura,
        'Keliones tipas': "egzotine"
 })

dfbaltictour_egzotine = pd.DataFrame(baltictour_egzotine)
dfbaltictour_egzotine.to_csv('baltictour.csv', index=False)

baltictour_pazintine=[]
target = 'https://www.baltictours.lt/kelioniu-kryptys/pazintines-keliones/'
response = requests.get(target)
soup = BeautifulSoup(response.content,'html.parser')



products = soup.find_all('div', class_='s2l-el special__offer')
for product in products:
    salis = product.find('div', class_='city').text.strip()
    regionas = product.find('div', class_='country').text.strip()
    trukme = product.find('div', class_='nights').text.strip().split(" ", 1)[0]
    kaina = product.find('div', class_='price').text.strip().replace('nuo\n','').split(" €")[0]
    reitingas_count = product.find('div', class_='stars')
    reitingas = str(reitingas_count).replace('<div class="stars stars-', '').replace('"></div>', '')
    data = product.find('div', class_='date').text.strip()[0:10]
    agentura = 'Baltictours'


    baltictour_pazintine.append({
        'Salis' : salis,
        'Regionas' : regionas,
        'Trukme' : trukme,
        'Kaina' : kaina,
        'Data' : data,
        'Reitingas' : reitingas,
        'agentura' : agentura,
        'Keliones tipas' : "pazintine"
 })

dfbaltictour_pazintine = pd.DataFrame(baltictour_pazintine)
dfbaltictour_pazintine.to_csv('baltictour_pazintine.csv', index=False)

baltictour_poilsine=[]
target = 'https://www.baltictours.lt/kelioniu-kryptys/poilsines-keliones/?min-price=262&max-price=600'
response = requests.get(target)
soup = BeautifulSoup(response.content,'html.parser')

products = soup.find_all('div', class_='s2l-el special__offer')
for product in products:
    salis = product.find('div', class_='city').text.strip()
    regionas = product.find('div', class_='country').text.strip()
    trukme = product.find('div', class_='nights').text.strip().split(" ", 1)[0]
    kaina = product.find('div', class_='price').text.strip().replace('nuo\n','').split(" €")[0]
    reitingas_count = product.find('div', class_='stars')
    reitingas = str(reitingas_count).replace('<div class="stars stars-', '').replace('"></div>', '')
    data = product.find('div', class_='date').text.strip()[0:10]
    agentura = 'Baltictours'

    baltictour_poilsine.append({
        'Salis' : salis,
        'Regionas' : regionas,
        'Trukme' : trukme,
        'Kaina' : kaina,
        'Data' : data,
        'Reitingas' : reitingas,
        'agentura' : agentura,
        'Keliones tipas' : "poilsine"
 })

dfbaltictour_poilsine = pd.DataFrame(baltictour_poilsine)
dfbaltictour_poilsine.to_csv('baltictour_poilsine.csv', index=False)

dfbendrasbaltic = pd.concat([dfbaltictour_pazintine, dfbaltictour_egzotine, dfbaltictour_poilsine], axis=0)
dfbendrasbaltic.to_csv('Bendrasbaltic.csv', index=False)


dfbendras = pd.concat([dfbendrasbaltic, dfbendraspanorama], axis=0)
dfbendras.to_csv('Bendraskeloniu.csv', index=False)
print(dfbendras)