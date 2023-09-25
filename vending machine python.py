item_list = {
"D1" :["coke",1.20],
"D2" :["fanta",1.20],
"D3" :["sprite",1.35],
"D4" :["pepsi",1.09],
"D5" :["pepsi max",1.09],
"D6" :["pepsi max cherry",1.09],
"C1" :["ready salted crisps",1.60],
"C2" :["salt and vinegar crisps",1.60]
}

balance = 0

print("Welcome")
print("Here are the items we offer at this vending machine:")
print()
for key, value in item_list.items():
    if key == "":
        print(key, "{:.2f}".format(value[1]))
    else:
        print(key, value[0], "{:.2f}".format(value[1]))
print()
print()
print("Your current balance is:",balance)


while True:
    try:
        balance = float(input("Please input the ammount of money you would like to input: "))
        if balance <= 0:
            print("Please enter an amount greater than 0")
        else:
            print("Your balance is now","{:.2f}".format(balance))
            print()
            break
    except ValueError:
        print("Invalid input. Please enter a valid numeric number.")


valid_item = False

while not valid_item:
    try:
        item_chosen = input("Please input the code for the item you would like to purchase:").upper()

        if item_chosen in item_list:
            item_price = item_list[item_chosen][1]
            if balance >= item_price:
                print("Item chosen:", item_list[item_chosen][0])
                print("Price of", item_list[item_chosen][0], "is {:.2f}".format(item_price))
                print("Your balance after purchase will be: {:.2f}".format(balance - item_price))
                print("Thank you")
                valid_item = True
            else:
                print("Insufficient balance to purchase", item_list[item_chosen][0],"Please try again")
        else:
            print("Invalid option. Please try again")
    except ValueError :
        print("Invalid input. Please enter a valid numeric number.")