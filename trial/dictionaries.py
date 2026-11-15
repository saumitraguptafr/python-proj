#Dictionary = a collection of {key:value} pairs, ordered and changeable no duplicates
capitals = {"USA":"Washington DC",
            "India":"New delhi",
            "China":"beijing",
            "Russia":"moscow"}

#print(dir(captials))-gives a set of function we can use
#print(help(captials))- explains those function mentioned above
#print(capitals.get("USA")) - gives the value assosciated to that key
#print(capitals.get("japan"))- gives "None" in ouput, as japan is not in dictionary
#to find out if a capital is there or not for a input of any country
#capital = input("Which countries capital do u want: ")
#if capitals.get(capital):
    #print("That capital exists")
#else:
    #print("That capital doesnt exists")

#capitals.update({"Germany":"berlin"})- updates or adds, in this case adds the key and value in to our dictonary
#capitals.update({"USA":"Ohio"})- in this case it updates the disctonary, specifically the value of "USA"
#capital = capitals.get("USA")
#print(capital)

#capitals.pop("China")- removes the selected key and value
#capitals.popitem()- removes the lastest key and value, in this case its russia and moscow
#capitals.clear()- removes every key and value in our disctionary

#keys = capitals.keys()- gives key in the form of list
#for key in keys:
    #print(key)- this entire loop gives the key but not in the form of the list
#values = capitals.values() - gives value in form of list

items = capitals.items()
#for item in items:
    #print(item)- print key and values in form of 2d list
for key, value in capitals.items():
    print(f"{key} : {value}")