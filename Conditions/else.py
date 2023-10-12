#else branching
x = float(input("Input the number: "))
y = float(input("input the number: "))

if x > y:
    print(f'{x} is greater than {y}')
elif x < y:
    print(f'{y} is greater than {x}')
else:
    print(f'{x} is equal to {y}')
