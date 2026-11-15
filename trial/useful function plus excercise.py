#name = input("what is ur full name? : ")
#phone_number = input("enter ur phone no: ")
#result = len(name)- gives the no of character strings in ur name, this includes spaces too
#result = name.find("u")- gives the posn of the letter from the left side, also the first letter starts with posn "0", so saumitra, posn of u is 2
#result =  name.rfind("a")- gives the posn of the letter from the reverse side hence the r, also if python doesnt find any letter it will show -1
#result = name.capitalize()- capatalises the first letter or string
#result = name.upper()- capatalises every letter 
#result = name.lower()- lowercases every letter
#result = name.isdigit()- it gives the output in true or false (boolean), if the input doesnt have any letters or spaces, it willl give true elsewise false
#result = name.isalpha()- gives true or false, if the input doesnt have any digits or spaces, it will give true, elsewise false
#result = phone_number.count("-")- it counts the no of (-) in the input
#phone_number = phone_number.replace("-", " ")- replaces the (-) with space string ( )
#note: ( ) is diff from ()
#print(help(str)) - gives u all of these function plus more to use



# EX :valid username- 12 charcters only, no spaces and no digits
username = input("please input ur username: ")
while username.isdigit():
    print("that username is not valid")
    username = input("please enter ur username: ")
print(f"hello {username}")
