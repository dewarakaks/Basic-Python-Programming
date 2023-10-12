#Python logical operators
x = int(input('input your birthday: '))
if x > 2000 and x <2010:
    print('you were born between 2000 and 2010')
elif x > 2010:
    print('you were born after 2010')
else:
    print(f'you were born in {x}')