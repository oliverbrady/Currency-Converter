import pickle
import re
import requests

def menu():
    print("Welcome to my currency software. You can convert your money and store it here.")
    global user_choice
    user_choice = input("\n1. Make an entry \n2. Review previous entries \n3. Exit\n"
                        "What would you like to do? ").lower()
    while menu:
        if user_choice in user_choice1:
            main()
        elif user_choice in user_choice2:
            record()
        elif user_choice in user_choice3:
            print("Goodbye!")
            exit()
        else:
            print("Sorry, I do not understand your request.\n")
            menu()

def main():
    print("\nAvailable Currencies: \nUS Dollars\nChinese Yuan\nEuros\nBritish Pounds\nTaiwanese Dollars\n")
    user_money = input("Enter a currency symbol, followed by the amount : ")
    if "exit" == user_money:
        exit()
    elif "menu" == user_money:
        menu()

    money_search = re.search(r'([\D]+)([\d]+)', user_money)

    while not money_search:
        user_money = input("Sorry, we do not recognise this currency. Please enter currency symbol before the number: ")
        money_search = re.search(r'([\D]+)([\d]+)', user_money)
        if "exit" == user_money:
            exit()
        elif "menu" == user_money:
            menu()

    global output
    output = (money_search.group(1), money_search.group(2))
    global final
    final = int(money_search.group(2))

    if '¥' == money_search.group(1):
        from_cny()
    elif '$' == money_search.group(1):
        from_usd()
    elif 'NT$' == money_search.group(1):
        from_twd()
    elif '£' == money_search.group(1):
        from_gbp()
    elif '€' == money_search.group(1):
        from_eur()
    else:
        print("\nI'm sorry, we do not currently recognise this currency.")

    stored_name = input("\nPlease give your money a name: ")
    stored_currency = input("\nDollars\nYuan\nEuros\nBritish Pounds\nTaiwanese Dollars\n"
                            "Please enter a preferred currency for your money: ").casefold()

    while stored_currency:
        if stored_currency in usd_set:
            named_result = "\n" + stored_name + ": " + usd_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in cny_set:
            named_result = "\n" + stored_name + ": " + cny_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in eur_set:
            named_result = "\n" + stored_name + ": " + eur_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in gbp_set:
            named_result = "\n" + stored_name + ": " + gbp_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in twd_set:
            named_result = "\n" + stored_name + ": " + twd_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        else:
            print("\nMy apologies, we do not recognise your statement.")
            stored_currency = input("Please enter a preferred currency for your money: ").lower()

    restart = input("\nWould you like to add more money? ").lower()
    if restart in yes_list:
        main()
    else:
        menu()

def record():
    user_read = open("user_record.txt", "r")
    print(user_read.read())
    user_read.close()
    menu_return = input("\nProcess finished.\n1. Menu 2. Clear List\n\nWhat would you like to do? ").lower()
    if menu_return in menu_tab:
        menu()
    elif menu_return in edit_tab:
        are_you_sure = input("Are you sure you would like to clear the list? ")
        if are_you_sure in yes_list:
            open('user_record.txt', 'w').close()
    else:
        print("Sorry, didn't quite catch that. You have been re-directed to the menu.")
        menu()

def from_cny():
    for item in range(1):
        global cny_formatted
        cny_formatted = "¥{:,.2f}".format(final)
        print("\nYour Chinese money: " + cny_formatted)
    for item in range(1):
        global usd_formatted
        cny_usd = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = cny_usd.json()
        usd = conversion_response['CNY_USD']
        usd_calculation = final * usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global eur_formatted
        eur_cny = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_cny.json()
        eur = conversion_response['EUR_CNY']
        eur_calculation = final / eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: " + eur_formatted)
    for item in range(1):
        global gbp_formatted
        gbp_cny = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_cny.json()
        gbp = conversion_response['GBP_CNY']
        gbp_calculation = final / gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: " + gbp_formatted)
    for item in range(1):
        global twd_formatted
        cny_twd = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = cny_twd.json()
        twd = conversion_response['CNY_TWD']
        twd_calculation = final * twd
        twd_formatted = "NT${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)

def from_usd():
    for item in range(1):
        global usd_formatted
        usd_formatted = "${:,.2f}".format(final)
        print("\nYour US money: " + usd_formatted)
    for item in range(1):
        global cny_formatted
        usd_cny = requests.get("https://free.currconv.com/api/v7/convert?q=USD_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = usd_cny.json()
        cny = conversion_response['USD_CNY']
        cny_calculation = final * cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global eur_formatted
        eur_usd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_usd.json()
        eur = conversion_response['EUR_USD']
        eur_calculation = final / eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: ", eur_formatted)
    for item in range(1):
        global gbp_formatted
        gbp_usd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_usd.json()
        gbp = conversion_response['GBP_USD']
        gbp_calculation = final / gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: ", gbp_formatted)
    for item in range(1):
        global twd_formatted
        usd_twd = requests.get("https://free.currconv.com/api/v7/convert?q=USD_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = usd_twd.json()
        twd = conversion_response['USD_TWD']
        twd_calculation = final * twd
        twd_formatted = "NT${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)

def from_twd():
    for item in range(1):
        global twd_formatted
        twd_formatted = "NT${:,.2f}".format(final)
        print("\nYour Taiwanese money: " + twd_formatted)
    for item in range(1):
        global usd_formatted
        usd_twd = requests.get("https://free.currconv.com/api/v7/convert?q=USD_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = usd_twd.json()
        usd = conversion_response['USD_TWD']
        usd_calculation = final / usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global cny_formatted
        cny_twd = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = cny_twd.json()
        cny = conversion_response['CNY_TWD']
        cny_calculation = final / cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global eur_formatted
        eur_twd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_twd.json()
        eur = conversion_response['EUR_TWD']
        eur_calculation = final / eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: ", eur_formatted)
    for item in range(1):
        global gbp_formatted
        gbp_twd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_twd.json()
        gbp = conversion_response['GBP_TWD']
        gbp_calculation = final / gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: ", gbp_formatted)

def from_gbp():
    for item in range(1):
        global gbp_formatted
        gbp_formatted = "£{:,.2f}".format(final)
        print("\nYour British money: " + gbp_formatted)
    for item in range(1):
        global usd_formatted
        gbp_usd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_usd.json()
        usd = conversion_response['GBP_USD']
        usd_calculation = final * usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global cny_formatted
        gbp_cny = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_cny.json()
        cny = conversion_response['GBP_CNY']
        cny_calculation = final * cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global eur_formatted
        gbp_eur = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_EUR&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_eur.json()
        eur = conversion_response['GBP_EUR']
        eur_calculation = final * eur
        eur_formatted = "€{:,.2f}".format(eur_calculation)
        print("Euros: ", eur_formatted)
    for item in range(1):
        global twd_formatted
        gbp_twd = requests.get("https://free.currconv.com/api/v7/convert?q=GBP_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = gbp_twd.json()
        twd = conversion_response['GBP_TWD']
        twd_calculation = final * twd
        twd_formatted = "NT${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)

def from_eur():
    for item in range(1):
        global eur_formatted
        eur_formatted = "€{:,.2f}".format(final)
        print("\nYour money in Euros: " + eur_formatted)
    for item in range(1):
        global usd_formatted
        eur_usd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_USD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_usd.json()
        usd = conversion_response['EUR_USD']
        usd_calculation = final * usd
        usd_formatted = "${:,.2f}".format(usd_calculation)
        print("US Dollars: ", usd_formatted)
    for item in range(1):
        global cny_formatted
        eur_cny = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_CNY&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_cny.json()
        cny = conversion_response['EUR_CNY']
        cny_calculation = final * cny
        cny_formatted = "¥{:,.2f}".format(cny_calculation)
        print("Chinese Yuan: ", cny_formatted)
    for item in range(1):
        global gbp_formatted
        eur_gbp = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_GBP&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_gbp.json()
        gbp = conversion_response['EUR_GBP']
        gbp_calculation = final * gbp
        gbp_formatted = "£{:,.2f}".format(gbp_calculation)
        print("British Pounds: ", gbp_formatted)
    for item in range(1):
        global twd_formatted
        eur_twd = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_TWD&compact=ultra&apiKey=7fc65abe0596fd124124")
        conversion_response = eur_twd.json()
        twd = conversion_response['EUR_TWD']
        twd_calculation = final * twd
        twd_formatted = "${:,.2f}".format(twd_calculation)
        print("Taiwanese Dollars: ", twd_formatted)

user_record = {}
yes_list = {"yes", "yeah", "yep", "okay", "alright", "ok", "sure", "y"}
edit_tab = {"edit list", "2. edit list", "2", "change list"}
menu_tab = {"1. menu", "1", "menu"}
user_choice1 = {"1", "make an entry", "1. make an entry"}
user_choice2 = {"2", "review previous entries", "2. review previous entries"}
user_choice3 = {"3", 'exit', "3. exit"}
usd_set = {"dollars", "usd", "us dollars", "bucks", "us", "american", "american money", "$"}
cny_set = {"yuan", "rmb", "chinese", "china", "chinese money", "¥", "cny"}
eur_set = {"euros", "eur", "european", "€"}
gbp_set = {"british pounds", "pounds", "quid", "british money", "gbp", "£"}
twd_set = {"taiwan dollars", 'taiwanese dollars', "twd", "taiwan money", "taiwan", "nt$"}
usd_result = None
cny_result = None
eur_result = None
gbp_result = None
twd_result = None

menu()