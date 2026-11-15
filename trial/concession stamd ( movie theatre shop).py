#Concession stand
menu = {"popcorn":13.4,
         "soda":1.1,
         "pizza": 45.9,
         "lemonade":2.45}
print("--------MENU-------")
for key, value in menu.items():
    print(f"{key:10}: £{value:.2f}")
print("-------------------")
cart = []
total = 0
while True:
    food = input("Enter the food (press q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) == None:
        print("This is not in the menu or type it properly")
    else:
        cart.append(food)
print("--------ORDER---------")
for food in cart:
    print(food, end=" ")
    total += menu.get(food)
print()
print(f"Total is £{total:.2f}")


       
        

              
