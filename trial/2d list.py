#2d list
#example:
fruits =     ["apple", "banana", "orange"]
vegetables = ["potato", "spinach", "tomato"]
meats =      ["fish", "chicken", "pig"]
#looks like a excel sheet with rows and coloumns
#now its just like coordination system
grocerries = [fruits,vegetables , meats]
#to get a certain eleemnt in the list-
#the first[] indicates the row and the second []indicates element in that row ( acts like a coloumn)
print(grocerries[0][1])
print(grocerries[0][2])
print(grocerries[1][0])
print()
# could also be represented as grocerries = [["apple", "banana", "orange"],["potato", "spinach", "tomato"],["fish", "chicken", "pig"] ]
#to give every element in all the lists combined-
for collection in grocerries:
    for food in collection:
        print(food)
print()
print()
print()
print()
#creating a two dimensional key pad in ur phone
row_1 = ("1","2","3")
row_2 = ("4","5","6")
row_3 = ("7","8","9")
row_4 = ("*","0","#")
numpad = (row_1,row_2,row_3,row_4)
for row in numpad:
    for number in row:
        print(number, end="")
    print()
