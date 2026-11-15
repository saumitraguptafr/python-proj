#indexing- accessing elements of a sequence using []
# formula [start: end : step]

credit_no = "1234-5678-9012"
#print(credit_no[2]) - in this code we only filled it with the start field, this basically gives the string character corresponding to the no typed in the brackets
#note- it starts from 0 not 1
#print(credit_no[0:4])- in this code we used the start and end field, so the ouput gives the string charcter of 0 to string charcter 4, but the end feild is exlucive, kinda like open bracket in maths wheras start is inclusive like square bracket maths.
#print(credit_no[:4])- same as the one above, putting no nmber in start feild, python assumes that it will be starting from the start
#print(credit_no[:])- printts the enitre thing, as python assumes u start from starting all way to the ending
#print(credit_no[: : 2])- step fucntion, in this code, it prints every two string charcter
#print(credit_no[-1])- this code means that it will print the first no from the right side rather than left side

#program to get the last 4 digits of crdit card no 
credit_card = input("Enter your credit card no : ")
result = credit_card[-4 : ]
print(result)