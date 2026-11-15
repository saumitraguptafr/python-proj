#for loop- basically like while loop but instead of infinite output it gives fixed no of output
# it helps to iterate over a range, string and character
#counting og 1 to 10, just like indexing, the end field is exclusive
for x in range(1,11):
   print(x)
#for reversing the countdown-
for x in reversed(range(1,11)):
    print(x)
#below code is free from for loop
print("happy new year")
#for iteration of charcters and strings- basiacally copies the character in the same order as written in single string at a time
credit_card = "1234-567-89-098"
for x in credit_card:
    print(x)

#u can also count the no in 2s or 3s or any other number, just like indexing
for x in range(1,11,2):
    print(x)

#Use of continue and break function- these functions can also be used in while loop
#continue- is it used to skip over a string
for x in range(1,20):
    if x == 13:
        continue
    print(x)
#break- it breaks the loop, as in the loop wouldnt go further if reaches the breaking charcter
for x in range(1,20):
    if x == 13:
        break
    print(x)