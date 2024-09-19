x=input("Введите х:")
print("x=", x)
y=input("Введите y:")
print("y=", y)
m=((int(x)**int(y)/int(x))-((int(y)/int(x))**1/3))
from math import fabs
equation=fabs(m)+(int(y)-int(x))
print("Ответ: ", equation)