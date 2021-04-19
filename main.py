import currency_conversion
import pickle
import re

# how to include all currencies

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
        currency_conversion.from_cny()
    elif '$' == money_search.group(1):
        currency_conversion.from_usd()
    elif 'NT$' == money_search.group(1):
        currency_conversion.from_twd()
    elif '£' == money_search.group(1):
        currency_conversion.from_gbp()
    elif '€' == money_search.group(1):
        currency_conversion.from_eur()
    else:
        print("\nI'm sorry, we do not currently recognise this currency.")

    stored_name = input("\nPlease give your money a name: ")
    stored_currency = input("\nDollars\nYuan\nEuros\nBritish Pounds\nTaiwanese Dollars\n"
                            "Please enter a preferred currency for your money: ").casefold()

    while stored_currency:
        if stored_currency in usd_set:
            named_result = "\n" + stored_name + ": " + currency_conversion.usd_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in cny_set:
            named_result = "\n" + stored_name + ": " + currency_conversion.cny_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in eur_set:
            named_result = "\n" + stored_name + ": " + currency_conversion.eur_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in gbp_set:
            named_result = "\n" + stored_name + ": " + currency_conversion.gbp_formatted
            print(named_result)
            user_append = open("user_record.txt", "a")
            user_append.write(named_result)
            user_append.close()
            print("The amount is now stored.")
            break
        elif stored_currency in twd_set:
            named_result = "\n" + stored_name + ": " + currency_conversion.twd_formatted
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