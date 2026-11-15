#nested loop- loop withing a loop
#how it looks like:
#outer loop():
#    inner loop():

#Example:
#for x in range(1,10):
    #print(x)
#but this gives each string in diff lines, if we want all of them in same line:
    # print(x , end= "")
#if we want a dash or space btween them, we would put dash and space in the inverted comma after "end" (end= "-")
#im order to repeatd 123456789, three times suppose
for x in range (1,4):
    for y in range (1,10):
        print(y, end = "")
#if we want to put new line after every rpeatition
    print()
#note- rememeber to change the variable in nested loops