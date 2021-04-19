import requests
import re
import json
import main

def from_cny():
    for item in range(1):
        global cny_formatted
        cny_formatted = "¥{:,.2f}".format(main.final)
        print("\nYour Chinese money: " + cny_formatted)
    for item in range(1):
        global usd_formatted
        cny_usd = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = cny_usd.json()
        usd = conversion_response['CNY_USD']
        usd_calculation = main.final * usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global eur_formatted
        eur_cny = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_cny.json()
        eur = conversion_response['EUR_CNY']
        eur_calculation = main.final / eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: " + eur_formatted)
    for item in range(1):
        global gbp_formatted
        gbp_cny = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_cny.json()
        gbp = conversion_response['GBP_CNY']
        gbp_calculation = main.final / gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: " + gbp_formatted)
    for item in range(1):
        global twd_formatted
        cny_twd = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = cny_twd.json()
        twd = conversion_response['CNY_TWD']
        twd_calculation = main.final * twd
        twd_formatted = "NT${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)

def from_usd():
    for item in range(1):
        global usd_formatted
        usd_formatted = "${:,.2f}".format(main.final)
        print("\nYour US money: " + usd_formatted)
    for item in range(1):
        global cny_formatted
        usd_cny = requests.get("https://free.currconv.com/api/v7/convert?q=USD_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = usd_cny.json()
        cny = conversion_response['USD_CNY']
        cny_calculation = main.final * cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global eur_formatted
        eur_usd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_usd.json()
        eur = conversion_response['EUR_USD']
        eur_calculation = main.final / eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: ", eur_formatted)
    for item in range(1):
        global gbp_formatted
        gbp_usd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_usd.json()
        gbp = conversion_response['GBP_USD']
        gbp_calculation = main.final / gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: ", gbp_formatted)
    for item in range(1):
        global twd_formatted
        usd_twd = requests.get("https://free.currconv.com/api/v7/convert?q=USD_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = usd_twd.json()
        twd = conversion_response['USD_TWD']
        twd_calculation = main.final * twd
        twd_formatted = "NT${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)

def from_twd():
    for item in range(1):
        global twd_formatted
        twd_formatted = "NT${:,.2f}".format(main.final)
        print("\nYour Taiwanese money: " + twd_formatted)
    for item in range(1):
        global usd_formatted
        usd_twd = requests.get("https://free.currconv.com/api/v7/convert?q=USD_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = usd_twd.json()
        usd = conversion_response['USD_TWD']
        usd_calculation = main.final / usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global cny_formatted
        cny_twd = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = cny_twd.json()
        cny = conversion_response['CNY_TWD']
        cny_calculation = main.final / cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global eur_formatted
        eur_twd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_twd.json()
        eur = conversion_response['EUR_TWD']
        eur_calculation = main.final / eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: ", eur_formatted)
    for item in range(1):
        global gbp_formatted
        gbp_twd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_twd.json()
        gbp = conversion_response['GBP_TWD']
        gbp_calculation = main.final / gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: ", gbp_formatted)

def from_gbp():
    for item in range(1):
        global gbp_formatted
        gbp_formatted = "£{:,.2f}".format(main.final)
        print("\nYour British money: " + gbp_formatted)
    for item in range(1):
        global usd_formatted
        gbp_usd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_usd.json()
        usd = conversion_response['GBP_USD']
        usd_calculation = main.final * usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global cny_formatted
        gbp_cny = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_cny.json()
        cny = conversion_response['GBP_CNY']
        cny_calculation = main.final * cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global eur_formatted
        gbp_eur = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_EUR&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_eur.json()
        eur = conversion_response['GBP_EUR']
        eur_calculation = main.final * eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: ", eur_formatted)
    for item in range(1):
        global twd_formatted
        gbp_twd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_twd.json()
        twd = conversion_response['GBP_TWD']
        twd_calculation = main.final * twd
        twd_formatted = "NT${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)

def from_eur():
    for item in range(1):
        global eur_formatted
        eur_formatted = "€{:,.2f}".format(main.final)
        print("\nYour money in Euros: " + eur_formatted)
    for item in range(1):
        global usd_formatted
        eur_usd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_usd.json()
        usd = conversion_response['EUR_USD']
        usd_calculation = main.final * usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global cny_formatted
        eur_cny = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_cny.json()
        cny = conversion_response['EUR_CNY']
        cny_calculation = main.final * cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global gbp_formatted
        eur_gbp = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_GBP&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_gbp.json()
        gbp = conversion_response['EUR_GBP']
        gbp_calculation = main.final * gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: ", gbp_formatted)
    for item in range(1):
        global twd_formatted
        eur_twd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_twd.json()
        twd = conversion_response['EUR_TWD']
        twd_calculation = main.final * twd
        twd_formatted = "${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)