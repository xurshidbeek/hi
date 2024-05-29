"""
3ta son ichidan yigindisi eng katta boltrgan 2ta son
"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a > b  and b > c :
    d = a + b
    print("eng kattasi a va b " , d)
elif a > b and c > b :
    c = a + c
    print("eng kattasi a va c " , c)
else:
    f = b +c
    print("eng kattasi b va c " , f )