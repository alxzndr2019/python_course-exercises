import math

a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
c= int(input("Enter value for c:"))

x1 = ( -b + math.sqrt(b ** 2 - 4 * a * c))/ (2 * a) 
x2 = (-b - math.sqrt(b **  2 - 4 * a * c))/ (2 * a )

print(x1)
print(x2)

