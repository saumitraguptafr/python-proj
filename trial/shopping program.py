foods = []
prices = []
total = 0

while True: 
    food = input("Enter the food (press q to quit): ")
    if food.lower() == "q":
        break
    else:
       price = float(input("Enter the price of the food :"))
       foods.append(food)
       prices.append(price)
    
print("--------YOUR CART---------")
for food in foods:
    print(food)
for price in prices:
    total = total + price
print(f"the total cost of ur cart is {total}")