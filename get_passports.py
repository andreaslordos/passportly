import requests
import os

country_codes = os.listdir("public/images/countries")
 
base_img_url = 'https://nomadcapitalist.com/wp-content/plugins/nomad-tools/passports/public/assets/img/passports/'

for country in country_codes:
    if len(country) == 2:
        print("doing",country)
        url = base_img_url + country + ".webp"
        r = requests.get(url)
        with open(f"public/images/countries/{country}/passport.webp", 'wb') as outfile:
            outfile.write(r.content)
        print("did", country)
        print("---")