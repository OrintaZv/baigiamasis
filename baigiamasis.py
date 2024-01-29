import requests
from bs4 import BeautifulSoup
import pandas as pd
baltictour=[]
target = 'https://www.baltictours.lt/kelioniu-kryptys/egzotines-keliones/'
response = requests.get(target)
soup = BeautifulSoup(response.content,'html.parser')
# print(response.status_code)


products = soup.find_all('div', class_='s2l-el special__offer')
for product in products:
    salis = product.find('div', class_='city').text.strip()
    regionas = product.find('div', class_='country').text.strip()
    trukme = product.find('div', class_='nights').text.strip().split(" ", 1)[0]
    kainaold = product.find('div', class_='price').text.strip().replace(' €','').replace('nuo\n','')
    reitingas = product.find('div', class_='stars').text.strip()
    agentura = 'Baltictours'

    if len(kainaold) > 4:
        kainabeakcijos = kainaold[0:4]
        kaina = kainaold[4:8]
    else:
        kainabeakcijos = kainaold
        kaina=kainaold

    baltictour.append({
        'Salis' : salis,
        'Regionas' : regionas,
        'Trukme' : trukme,
        'Kaina' : kaina,
        'Kaina be Akcijos': kainabeakcijos,
        'reitingas' : reitingas,
        'agentura' : agentura
 })

dfbaltic = pd.DataFrame(baltictour)
dfbaltic.to_csv('keliones.csv', index=False)




kelioniupanorama=[]
for i in range(1,4):
    target = f"https://www.kelioniupanorama.lt/{i}?types=4&order=expensive"
    response = requests.get(target)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(target)


products = soup.find_all('a', class_='c-trip__details')
for product in products:
    salis_regionas = product.find('div', class_='c-trip__description').find('p').text.strip().split(',')
    salis = salis_regionas[0].strip()
    regionas = salis_regionas[1].strip()
    data_trukme = product.find('div', class_='c-trip__info').text.strip().split()
    data = data_trukme[0].strip()
    trukme = data_trukme[1].strip()
    kaina = product.find('div', class_='c-trip__price').text.strip().replace(' €','')
    # reitingas = product.find('div', class_='icon-star-3').text.strip()
    agentura = 'Kelioniu panorama'
    #print(products)

    kelioniupanorama.append({
        'Salis' : salis,
        'Regionas' : regionas,
        'Trukme': trukme,
        'Data' : data,
        'Kaina' : kaina,
        # 'Reitingas' : reitingas,
        'agentura': agentura
})

dfagentura = pd.DataFrame(kelioniupanorama)
dfagentura.to_csv('kelioniupanorama.csv', index=False)


dfbendras = pd.concat([dfbaltic, dfagentura], axis=0)
dfbendras.to_csv('Bendraskeloniu.csv', index=False)
print(dfbendras)