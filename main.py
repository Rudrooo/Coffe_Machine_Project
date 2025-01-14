MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 600,
    "milk": 500,
    "coffee": 700,
    "money":0
}

is_on=True

def check_resources(r,c):
    for i in r:
        if i=="money":

            break
        if r[i]<c[i]:
            print(f"Sorry there is not enough {i} ")
            return False
    return True

def money_check(m):
    q=int(input("How many quarters?: "))
    d=int(input("How many dimes?: "))
    n=int(input("How many nickles?: "))
    p=int(input("How many pennies?: "))
    money=q*0.25+d*0.10+n*0.05+p*0.01
    if money>m:
        return [True,money-m]
    else:
        return [False,money]

def resource_edit(resouce, ingredients, cost):
    for i in resouce:
        if i=="money":
            resouce[i]+=cost
            break
        resouce[i]-=ingredients[i]




while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    try:
        if choice== "report":
            print(resources)
        elif choice=="off":
            is_on=False

        else:
            coffe_i=MENU[choice]

            if check_resources(resources,coffe_i["ingredients"]):
                mm=money_check(coffe_i["cost"])
                if mm[0]:
                    print(f"Here is ${round(mm[1],2)} in change.")
                    print(f"Here is you {choice} 🍵☕🍵.Enjoy!")
                    resource_edit(resources, coffe_i["ingredients"],coffe_i["cost"])

                else:
                    print("Sorry that's not enough money. Money refunded.")
    except:
        print("Invalid input.Try again.")


