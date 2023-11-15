#not condition
birth_year = int(input('your birth year is: '))
print(f'The birth year is : {birth_year}')

if birth_year < 2001 or birth_year == 2002 or birth_year == 2003:
    print(f'you were born in {birth_year}')
else:
    print(f'you were born in {birth_year} is wrong')