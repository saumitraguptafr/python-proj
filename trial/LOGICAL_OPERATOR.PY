#logical operator= evulate multiple condtion (and,or not)
#or- if only one condition is true the whole statement is true
#and- if both condition is true then only the entire state,emt is considered true
#not - inverts the conditon (not false, not true)

#or
#temp= 9
#is_raining = False 
#if temp > 35 or temp < 0 or is_raining:
   #print("the outdoor event is cancelled")
#else:
   #print("the outdoor event is still sheduled")

#and
#temp = 25
#i_sunny=True

#if temp>= 38 and i_sunny:
    #print("it is hot and sunny outside")

#elif 38> temp > 0 and i_sunny:
    #print("its normal")

#else:
    #print("bla bla")

#not
temp = 25
is_sunny = False

if temp >= 30 and is_sunny:
    print("its sunny and hot")
elif 30> temp > 0 and is_sunny:
    print("its normal and sunny")
elif temp < 0 and is_sunny:
    print("its cold and sunny")
elif temp >= 30 and  not is_sunny:
    print("its not sunny and hot")
elif 30> temp > 0 and not is_sunny:
    print("its normal and  not sunny")
elif temp < 0 and  not is_sunny:
    print("its cold and  not sunny")