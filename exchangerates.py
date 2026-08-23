print("how much money will you have in different currencies?")

USD = float(1)
AED = float(3.67)
EGP = float(50.55)
JPY = float(162.25)
EUR = float(0.87)
SAR = float(3.76)
availablecurrencies = {"USD", "AED", "EGP", "JPY", "EUR", "SAR"}

print("Here is the list of the available currencies: USD, AED, EGP, JPY, EUR, SAR")

currency1 = input("pick a currency, and type it accurately: ")
while currency1 not in availablecurrencies:
    print("You need to select one of the available currencies")
    currency1 = input("Select the starting currency again: ")

if currency1 == 'USD'   : currency1 = USD
elif currency1 == 'AED' : currency1 = AED
elif currency1 == 'EGP' : currency1 = EGP
elif currency1 == 'JPY' : currency1 = JPY
elif currency1 == 'EUR' : currency1 = EUR
elif currency1 == 'SAR' : currency1 = SAR

currency2 = input("pick the currency you want to convert it to: ")
while currency2 not in availablecurrencies or currency1 == currency2:
    if currency2 not in availablecurrencies:
        print("You need to select one of the available currencies")
    else:
        print("You need to select two different currencies")
    currency2 = input("Select the target currency again: ")

if currency2 == 'USD'   : currency2 = USD
elif currency2 == 'AED' : currency2 = AED
elif currency2 == 'EGP' : currency2 = EGP
elif currency2 == 'JPY' : currency2 = JPY
elif currency2 == 'EUR' : currency2 = EUR
elif currency2 == 'SAR' : currency2 = SAR

amount = float(input("How much miney do you want to convert? "))
final = amount * currency2 / currency1
print(round(final, 2))
