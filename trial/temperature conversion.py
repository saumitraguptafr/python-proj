temperature = float(input("what is the temp:"))
unit = input("what is the units of of the temp(f/c/k): ")
if unit == "":
    print("please select a unit")
elif unit == "f":
    temperature = round(temperature * 9/5 + 32,2)
    print(f"the temperature is {temperature} F")
elif unit == "c":
    print(f" the the temperature is {temperature} C")
elif unit == "k":
    temperature = round(temperature + 273.15, 2)
    print(f"the temperature is {temperature} K")
else:
    print(f"{unit} is not valid")
