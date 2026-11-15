#while loop- it excutes some code as long as the condition remains true
#name = input("What is ur name : ")
#if name == "":
    #print("u dindt enter ur name")
    #name = input("enter ur name: ")- wiritng this woundlt cahnge a thing as even if u write or u dont write ur name here the program wont do anzthing abt it
#else:
   # print(f"hello {name}")
#if u want to continue to prompt the user into writing their name then u use while loop
#while name =="":
    #print("you did not enter ur name")
    #name = input("enter ur name: ")
#print(f"hello {name}")

food = input("what is ur fav food (press q to quit): ")
while not food =="q":
    print(f"ur fav food is {food}")
    food = input("ur other fav food is: ")
print("goodbye")
#just like if and else, you can also use or, and and not in while loop