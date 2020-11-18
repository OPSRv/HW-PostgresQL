from lib.db_manager import *
import requests
URL = "https://api.covid19api.com/summary"
response = requests.get(URL)
url = response.json()


def menyu(url):
    exit = True
    while exit:
        vyb = int(
            input("1. Вивести дані COVID 19 \t2. Обновити дані COVID 19\t0. EXIT => "))
        if vyb == 1:
            vyb2 = int(input("1.Вивести дані \"КРАЇНИ\"\t2. All countries => "))
            vyb_Country = 0
            con = "0"
            coc = "0"
            if vyb2 == 1:
                vyb_Country = int(
                    input("1. Country Name\t2. Country Code => "))
                if vyb_Country == 1:
                    con = input("Country Name => ")
                    coron_db.zap(covid_19_data)
                    coron_db.vyvid(vyb_Country, con, coc)
                elif vyb_Country == 2:
                    coc = input("Country Code => ")
                    coron_db.zap(covid_19_data)
                    coron_db.vyvid(vyb_Country, con, coc)
            elif vyb2 == 2:
                coron_db.zap(covid_19_data)
                coron_db.vyvid(vyb_Country, con, coc)
        if vyb == 2:
            zap(url)
            print("Update coron GOOD")
        elif vyb == 0:
            exit = False


menyu(url)
