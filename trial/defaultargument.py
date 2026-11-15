#There are 4 types of argument: 1.positional, 2.default, 3. keyword, 4. arbituary
#the postional one, we alrdy used that in function.py where u had to put same amount of arguemnt parameter and order matter
#default arguemnt: makes the function more flexible, dont need same amount of argument as parameter as in reduces parameter
def net_price(price,discount=0,tax=0.05):
    return price * (1-discount) * (1 + tax)
#print(net_price(500))
#as shown, we have lesser argument, and our discount and taxes are premeediated, but what if a customer has a coupon:
print(net_price(500,0.05))
#our argument has more priority than the one we alrdy set



#also default paramater must be after postional for the code to WORK


