"""
a b c sonlar berilgan kopayish yoki kanmayish tartibda bolsa ikkilantiring unday bolmasa ishorani ozgrtr
"""
a = int(input(" a = "))
b = int(input(" b = "))
c = int(input(" c = "))
if a < b < c or a > b >c :
    a = a *2
    b = b * 2
    c = c * 2
    print("bu sonlar kopyish yoki kamayish tartibda =  ", a, b ,c )
else:
    a = 0
    b = 0
    c = 0
    print("bu sonlar kopayish yoki kamayish tartibda emas",a , b, c )