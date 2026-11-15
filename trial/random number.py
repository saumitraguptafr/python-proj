import random
#print(help(random))- gives access to all random related function
#in order to get a random integer, we use:-
#number= random.randint(1,6)- for example we roll a dice
#print(number)- clicking play everytime will lead to diff results everytime
#low = 1
#high = 100
#number= random.randint(low,high)
#print(number)
#number = random.random()- gives a random float point between 0 and 1
#we can also randomize variable
#options = ("scissors", "rock", "paper")
#option = random.choice(options)
#print(option)
#there is also a shuffle option, we can shuffle or change the order
#cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#random.shuffle(cards)
#print(cards)
# obvio that () wont work cause tuple is unchangable

#NUMBER GUESSING GAME
low = int(input("whats the lower linit for the game?: "))
high = int(input("whats the higher linit for the game?: "))
number = random.randint(low,high)
guesses = 0
while True:
    guess = input("What do u think the no is?(press q to give up) : ").lower()
    guesses +=1
    if guess == "q":
        print(f"The number is {number}")
        break
    elif guess.isdigit() is not True:
         print("please choose an valid guess!")
    elif int(guess) < low or int(guess) > high:
            print("Please guess a number in the range!")
    elif int(guess) > number:
        print("Too high, try again!")
    elif int(guess) < number:
        print("Too low, try again!")
    elif int(guess) == number:
        print("DING DING, you have successfully guess the number!")
        break
total = guesses
print(f"You took a total of {total} tries!")