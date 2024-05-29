"""
3ta son berilgann ularning ortanchasini toping
"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a < b and a > c :
    print("o'rtachasi a")
elif b < a and b > c :
    print("o'rtachasi b")
else:
    print("o'rtachasi c")