#if : do some code only if some condition is true else do something else
#age = int(input("what is ur age? :"))
#if age >=45: (read as greater than or equal to)
    #print("you are too old")

#elif age >= 18:
    #print("u are elligible to vote")
#else :
    #print("u cannot vote")

#elif- this fucntion is basically used to add more conditions, rmemebr order matters in this and the function menetioned above
#first if statemnt comes, then elif statements and at the end else

#==( comparison function)- this is used instead of = in the if statement if instead of comparing variable to a integer,
#it is compared to a string (if straight == "yes")

answer = input("would u like some food(y/n):" )
if answer == "y":
    print("here have some")
else:
    print("ok")

name = input("what is ur name?:")
if name == "":
    print("you havent typed anything")
else:
    print(f"hello {name}")
