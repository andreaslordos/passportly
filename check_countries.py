from os import stat, listdir, remove, rmdir

country_codes = listdir("public/images/countries")

for country in country_codes:
    if len(country) == 2:
        file_stat = stat(f"public/images/countries/{country}/passport.webp")
        if file_stat.st_size < 1000:
            print(country)
            for file in listdir(f"public/images/countries/{country}"):
                remove(f"public/images/countries/{country}/{file}")
            rmdir(f"public/images/countries/{country}")

new_country_codes = listdir("public/images/countries")

for c in new_country_codes:
    print(f'"{c}",')