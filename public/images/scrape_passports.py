import os
import requests
import shutil
from time import sleep

countries = os.listdir("countries")

BASE_URL = "https://www.passportindex.org/countries/{country}.png"
for c in countries:
    if 'passport_new.png' not in os.listdir(f"countries/{c}"):
        url = BASE_URL.format(country=c)
        print(url)
        data = requests.get(url).content 
        f = open(f'countries/{c}/passport_new.png','wb') 
        f.write(data)
        f.close()
        print(f"wrote {c}")
        sleep(1)
    else:
        if os.path.getsize(f'countries/{c}/passport_new.png') < 30000:
            shutil.rmtree(f'countries/{c}')