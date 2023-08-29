weight = float(input("weight: "))
unit = input("(K)g) or L(bs): ")
if unit.upper ()== "K":
    converted = weight * 2.2
    print("Your weight in Lbs  " + str(converted))
else :
    converted = weight / 2.2
    print("Your weight in Kg  " + str(converted))