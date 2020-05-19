#
#   Coffee Machine
#


class CoffeeMachine():

    water_in_stock = 0
    milk_in_stock = 0
    coffee_bean_in_stock = 0
    money = 0
    disposable_cups = 0

    def __init__(self, water, milk, coffee_bean, price):
        self.water = water
        self.milk = milk
        self.coffee_bean = coffee_bean
        self.price = price

    def fill(self, water, milk, coffee_bean, disposable_cups):
        CoffeeMachine.water_in_stock += water
        CoffeeMachine.milk_in_stock += milk
        CoffeeMachine.coffee_bean_in_stock += coffee_bean
        CoffeeMachine.disposable_cups += disposable_cups

    # returning string for print, could have printed here
    # just keeping interaction with stdin/stdout minimal
    def take(self):
        temp = CoffeeMachine.money
        CoffeeMachine.money = 0
        return f"I gave you ${temp}"

    def buy(self):
        if CoffeeMachine.water_in_stock < self.water:
            return "Sorry, not enough water!"
        if CoffeeMachine.milk_in_stock < self.milk:
            return "Sorry, not enough milk!"
        if CoffeeMachine.coffee_bean_in_stock < self.coffee_bean:
            return "Sorry, not enough coffee beans"
        if CoffeeMachine.disposable_cups == 0:
            return "Sorry, not enough disposable cups"

        CoffeeMachine.water_in_stock -= self.water
        CoffeeMachine.milk_in_stock -= self.milk
        CoffeeMachine.coffee_bean_in_stock -= self.coffee_bean
        CoffeeMachine.money += self.price
        CoffeeMachine.disposable_cups -= 1
        return "I have enough resources, making you a coffee!"

    def __str__(self):
        string =  f'''The coffee machine has:
{CoffeeMachine.water_in_stock} ml of water
{CoffeeMachine.milk_in_stock} ml of milk
{CoffeeMachine.coffee_bean_in_stock} g of coffee beans
{CoffeeMachine.disposable_cups} of disposable cups
${CoffeeMachine.money} of money'''
        return string


# three object of CoffeeMachine
espresso = CoffeeMachine(250, 0, 16, 4)
latte = CoffeeMachine(350, 75, 20, 7)
cappuccino = CoffeeMachine(200, 100, 12, 6)

# initial resources
espresso.fill(400, 540, 120, 9)
CoffeeMachine.money = 550


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "remaining":
        print()
        print(espresso)
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

        if action == 1:
            print(espresso.buy())
        elif action == 2:
            print(latte.buy())
        else:
            print(cappuccino.buy())
        print()
    elif action == 'fill':
        print()
        print("Write how many ml of water do you want to add:")
        water = int(input())
        print("Write how many ml of milk do you want to add:")
        milk  = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        coffee_bean  = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        disposable_cups  = int(input())
        espresso.fill(water, milk, coffee_bean, disposable_cups)
        print()
    else:
        print()
        print(espresso.take())
        print()
