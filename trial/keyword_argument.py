#keyword argument- one of the 4 arguments, this one has the benift of easy readability, argument order doesnt matter
#first without keyword argument ( positional argument: postion matters)
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")
#hello("hello", "mr.", "saumit", "gupta")
#in order to make keyword argument 
hello("hello", title="mr.", first="saumit", last= "gupta")


#JUST LIKE DEFAULT POSTIONAL SHOULD BE PLACED AT FIRST (hello) then rest of the argument



#print(x, end="")- where end is a keyword arguemnt
print("1", "2", "3", sep="-")