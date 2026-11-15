principle = float(input("Enter princple no :"))
while principle <= 0:
    principle = float(input("Enter princple no :"))
    if principle <= 0:
        print(" principle cannot be less than or equal to zero")
rate = float(input("Enter rate :"))
while rate <= 0:
    rate = float(input("Enter rate :"))
    if rate <= 0:
        print(" rate cannot be less than or equal to zero")
time = float(input("Enter no of years  :"))
while time < 0:
    time = float(input("Enter no of years:"))
    if time < 0:
        print(" no of years cannot be less than 0")

result = principle * pow(1 + rate / 100, time)
print(f" the amount after {time} year(s) : {result}")
