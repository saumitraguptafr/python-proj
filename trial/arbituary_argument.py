#abrituary arguments
# *args - allows you to pass multiple non-keyword arguments, also the class of args in tuple
# **kwargs - allows you to pass multiple keyword argument, also the class of kwargs is dictionary
# * this sign means an unpacking operator
#suppose i want to make a prgram to add two number
#def add(a,b):
    #return a + b
#print(add(2,3))
#but what if i add three arguments 
#like add(1,2,3), then it will show error to solve this we use arbituary arguments
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(2,3,4))
#so now it would add, we dont need to name it only *args, it would work for any name as long as * is in font (*nums)


#NOW FOR KWARGS
#value will give us the the adress i put as in (blf street 45679 new delhi India)
def home_address(**kwargs):
    for value in kwargs.values():
        print(value)

home_address(street="blf street", zip = "45679", city = "new delhi", country = "India")
#key will give (street zip city country as ouput) [for key in kwargs.keys()]
# for key,value in kwargs.items() will give :(street="blf street", zip = "45679", city = "new delhi", country = "India"

#TO HAVE BOTH KWARGS AND ARGS IN UR PARMATER MAKE SURE TO KEEP *ARG FIRST THEN **KWARGS as in home_address(*args, **kwargs)