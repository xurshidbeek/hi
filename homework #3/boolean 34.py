# boolean 36

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

if (1 <= x1 <= 8 and 1 <= y1 <= 8) and (1 <= x2 <= 8 and 1 <= y2 <= 8):
    if (x1 == x2 and y1 != y2) or (y1 == y2 and x1 != x2):
        print("Yura oladi")
    else:
        print("Yura olmaydi")

else:
    print("Error")
