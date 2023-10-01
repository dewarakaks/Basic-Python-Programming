def cmp(t1,t2):
    return bool(t1 > t2) - bool(t1 < t2)
def cmp(t3,t4):
    return bool(t3 > t4) - bool(t3 < t4)
def cmp(t5,t6):
    return bool(t5 > t6) - bool(t5 < t6)
t1 = (1,2)
t2 = (1,2)

t3 = (6)
t4 = (5)

t5 = (1)
t6 = (1)

print(cmp(t1,t2))
print(cmp(t3,t4))
print(cmp(t5,t6))