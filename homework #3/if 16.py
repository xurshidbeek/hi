"""
a, b, c sonlar berlgan agar u sonla osish tartibida bolsa
sonlarni ikkilantiring aks holda ishorasini ozgarti

"""
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a <  b < c:
    c = b * 2
    f = a * 2
    g = c * 2
    print("sonlar osish tartibida " , c , f , g )

else:
    a = a * -1
    b = b * -1
    c = c * -1
    print("sonlar osish tartibida emas " , a , b , c)

