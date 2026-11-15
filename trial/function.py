#function- A blovk of reuseable code, place () after the function name to invoke it.
#i wanna print happybirthday song three time
#1st way: print it three times
#2nd way- using loop 
#3rd way- using function:
#def happy_birthday():
    #print("Happy Birthday to you!")
    #print("Happy Birthday to you!")
    #print("May god bless you")
    #print("Happy Birthday to you!")
    #print()
#happy_birthday()
#happy_birthday()
#happy_birthday()
#Just make sure to nest the code u wanna reuse
#you can also set parameter
def happy_birthday(name):
    print(f"Happy Birthday to {name} !")
    print(f"Happy Birthday to {name}!")
    print(f"May god bless {name}")
    print(f"Happy Birthday to {name}!")
    print()
happy_birthday("saumit")
happy_birthday("sanvi")
happy_birthday("chinku")
#name is he parameter and "saumit" is the argument
#you can also put integer along with the string but for that u will need to define two parameter one for string (name) and one for the age (age)
#where saumit and, 18 are argument
def happy_birthday(name,age):
    print(f"Happy Birthday to {name} !")
    print(f"Happy Birthday to {name}!")
    print(f"May god bless {name}")
    print(f"You are old {age}")
    print(f"Happy Birthday to {name}!")
    print()
happy_birthday("saumit", 18)
happy_birthday("sanvi",14)
happy_birthday("chinku",13)
#BUT THE POSTION OF PARAMETER AND ARGUMENT MATTERS SUPPOSE AGE AND NAME ARE SWITCHED:-
def happy_birthday(age,name):
    print(f"Happy Birthday to {name} !")
    print(f"Happy Birthday to {name}!")
    print(f"May god bless {name}")
    print(f"You are old {age}")
    print(f"Happy Birthday to {name}!")
    print()
happy_birthday("saumit", 18)
happy_birthday("sanvi",14)
happy_birthday("chinku",13)
#this what the result would have been:-(chinku example)
#Happy Birthday to 13 !
#Happy Birthday to 13!
#May god bless 13
#You are old chinku
#Happy Birthday to 13!