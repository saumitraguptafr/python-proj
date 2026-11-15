#collection- single "variable" used to store multiple values
#can be done in 3 ways
#List- denoted by [], ordered and changeable, Dupilcates OK
# set- denoted by {}, un ordered and immutable(changeable), but add/remove OK, No duplicates
#tiple- (), ordered, unchangelable, duplicates OK. faster
#example

#List:
fruits = ["apple", "oranges", "banana"]
#print(fruits)
#you can access each fruit by indexing
#print(fruits[0: 4 : 2])
#length function gives the no of elements in the list
#print(len(fruits))
#in opertaor: you can use this to see if a specific element is in the list, gives a boolean ans
#print( "pineapple " in fruits)
#now as it is changelable- the code below changes the first element to whatever we want
#fruits[0] = "pineapple"
#for x in fruits:
   #print(x)
#to add more ements
#fruits.append("mango")
#to add an element inb a specific position, we sue insert function
#fruits.insert(0, "blueberry")
#to remove an element
#fruits.remove("mango")
#to sort the element in alphabetical order,if first letter is same then it goes to other letter
#fruits.sort()
#to reverse the order in which the fruits are currently in (after sortin, if sorting wasnt used it was reverse the order prior to that)
#fruits.reverse()
#to remove all elements
#fruits.clear()
#to find a index of a element, it shows index not of the orgianl one in the start
#print(fruits.index("blueberry"))
#to count how many particular eleement is there
#print(fruits.count("banana"))


#SETS
cars = {"BMW", "Lamborghini", "ferrari", "bugatti", "BMW"}
#print(cars)
#on printing it is noticed that the output order is diff than the order we gave input and running the print again will show a diff order
#print(len(cars))- gives no of elemnts in cars varaiable
#print( "BMW" in cars)- works same as above
#NOTE : indexing is not allowed it will give error
#print(cars[0])
#add and rmeove like above works
#to remove the first element of the order, but since order is variable in this, the element removed is variable too
cars.pop()  
#print(cars)
#print(cars.count("BMW"))- DOES NOT WORK
#u can clear all elements using the clear function like above
#if there are two same elemnts or a element repeated tiwce in our set, it is only shown once upon printing

#Tuple: basically like list but u cant add or remove anything
countries = ("india", "israel", "usa", "iran", "iran")
#print(countries[0])- works
#print(countries.count("iran"))- works
#for loop also works, it lists all elements