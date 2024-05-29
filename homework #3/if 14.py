"""
3ta son berilgan avval kichigini keyin kattasini choqaruvchi
"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a < b and a < c :
    print("eng kichigi a ")
elif b < a and b <c :
    print("eng kichigi b ")
else:
    print("eng kichigi c ")
if b > a and b > c :
    print("eng kattasi b")
elif a > c and a > b :
    print("eng kattasi a")
else:
    print("eng kattasi c ")