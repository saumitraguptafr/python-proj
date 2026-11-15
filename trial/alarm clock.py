import time
#time.sleep(2)- this function basically means the program will sleep for 2 seconds and then start the codes written later
my_time = int(input("enter the no of seconds: "))
for x in reversed(range(0, my_time + 1)):
    time.sleep(1)
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Times up!")

