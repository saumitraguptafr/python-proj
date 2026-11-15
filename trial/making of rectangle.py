rows = int(input(" enter no of rows : "))
coloumns = int(input(" enter no of coloumns : "))
symbols = input("eneter s symbol to use : ")
for x in range(rows):
    for y in range(coloumns):
        print(symbols, end = "")
    print()