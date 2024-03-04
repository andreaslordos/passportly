from os import stat, listdir, remove, rmdir

country_codes = listdir("countries")

for country in country_codes:
    if len(country) == 2:
        file_stat = stat(f"countries/{country}/passport.webp")
        if file_stat.st_size < 1000:
            print(country)
            for file in listdir(f"countries/{country}"):
                remove(f"countries/{country}/{file}")
            rmdir(f"countries/{country}")

new_country_codes = listdir("countries")

for c in new_country_codes:
    print(f'"{c}",')