#conditional expression: a one line shortcut for the if-else statemnt
# formula: (X) if (condition) else (Y): read as the ouput would be statemnt x or x if the condioton is staisfied or esle it gives y

num = 5
a=6
b=7
age = 18
user_role = "admin"
#print ( "postive" if num > 0 else "negative")
#print("even" if num % 2 == 0 else "odd")
max_val = b if a < b else a
min_val = a if a < b else b
#print(max_val)
#print(min_val)
#print("You can vote" if age >= 18 else "you are still a child, you cannot vote")
print("You are cleared" if user_role == "admin" else "you are not cleared")