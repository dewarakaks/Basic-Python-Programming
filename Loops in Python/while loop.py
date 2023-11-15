# using while loopfunction in python
# aksi ini
# aksi itu
# print

x = [2001,2002,2003,2004,2005]

index = 0
tahun = x[0]

while tahun != 2003:
    print(tahun)
    index += 1
    tahun=x[index]
print('hanya dapat', index, 'untuk berhenti dari perulangan')