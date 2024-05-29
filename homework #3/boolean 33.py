a = int(input(" a= "))
b = int(input(" b= "))
c = int(input(" c= "))

if((a + b > c or a + c > b or b + c > a) and (c > abs (a - b) or b > abs ( a - c ) or a > abs ( b-c ))):
    print(f"{a},{b},{c} lardan uchburchak yasash mumkin")
else:
    print(f"{a},{b},{c} lardan uchburchak yasash mumkin emas")
