#
#   Coffice Machine
#   without using class


water_in_stock = 400
milk_in_stock = 540
coffee_bean_in_stock = 120
money = 550
disposable_cups = 9

espresso_water = 250
espresso_milk = 0
espresso_coffee = 16
espresso_price = 4

latte_water = 350
latte_milk = 75
latte_coffee = 20
latte_price = 7

cappuccino_water = 200
cappuccino_milk = 100
cappuccino_coffee = 12
cappuccino_price = 6


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "remaining":
        print()
        print("The coffee machine has:")
        print(f'{water_in_stock} ml of water')
        print(f'{milk_in_stock} ml of milk')
        print(f'{coffee_bean_in_stock} g of coffee beans')
        print(f'{disposable_cups} of disposable cups')
        print(f'${money} of money')
        print()
    elif action == 'exit':
        break
    elif action == 'buy':
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        action = input()
        if action == 'back':
            print()
            continue
        else:
            action = int(action)
        if action == 3:
            if water_in_stock < cappuccino_water:
                print("Sorry, not enough water!")
                print()
                continue
            if milk_in_stock < cappuccino_milk:
                print("Sorry, not enough milk!")
                print()
                continue
            if coffee_bean_in_stock < cappuccino_coffee:
                print("Sorry, not enough coffee beans")
                print()
                continue
            if disposable_cups < 1:
                print("Sorry, not enough disposable cups")
                print()
                continue
            water_in_stock -= cappuccino_water
            milk_in_stock -= cappuccino_milk
            coffee_bean_in_stock -= cappuccino_coffee
            money += cappuccino_price
        elif action == 2:
            if water_in_stock < latte_water:
                print("Sorry, not enough water!")
                print()
                continue
            if milk_in_stock < latte_milk:
                print("Sorry, not enough milk!")
                print()
                continue
            if coffee_bean_in_stock < latte_coffee:
                print("Sorry, not enough coffee beans")
                print()
                continue
            if disposable_cups < 1:
                print("Sorry, not enough disposable cups")
                print()
                continue
            water_in_stock -= latte_water
            milk_in_stock -= latte_milk
            coffee_bean_in_stock -= latte_coffee
            money += latte_price
        else:
            if water_in_stock < espresso_water:
                print("Sorry, not enough water!")
                print()
                continue
            if milk_in_stock < espresso_milk:
                print("Sorry, not enough milk!")
                print()
                continue
            if coffee_bean_in_stock < espresso_coffee:
                print("Sorry, not enough coffee beans")
                print()
                continue
            if disposable_cups < 1:
                print("Sorry, not enough disposable cups")
                print()
                continue
            water_in_stock -= espresso_water
            milk_in_stock -= espresso_milk
            coffee_bean_in_stock -= espresso_coffee
            money += espresso_price
        disposable_cups -= 1
        print("I have enough resources, making you a coffee!")
        print()
    elif action == 'fill':
        print()
        print("Write how many ml of water do you want to add:")
        water_in_stock += int(input())
        print("Write how many ml of milk do you want to add:")
        milk_in_stock  += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        coffee_bean_in_stock  += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        disposable_cups  += int(input())
        print()
    else:
        print()
        print(f"I gave you ${money}")
        print()
        money = 0

