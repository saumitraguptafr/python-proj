#python calcultor
operator = input(" please slect( + - / *):")
num_1 = float(input("what is ur number? :"))
num_2 = float(input("whats is ur other number? :"))

if operator == "":
    print("please slect one operator")

elif operator == "+":
    c = num_1 + num_2
    print(f"{c}")
elif operator == "-":
    c = num_1 - num_2
    print(f"{c}")
elif operator == "/":
    c = num_1 / num_2
    print(f"{c}")
elif operator == "3":
    c = num_1 * num_2
    print(f"{c}")
else :
    print( "not a valid opertaor")


