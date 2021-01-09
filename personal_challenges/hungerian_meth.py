#PHASE 1

## take a values

print('-a1-|-a2-|-a3-|-a4-\n -b1-|-b2-|-b3-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-')

a1 = int(input("Enter number for cell a1:")
)
print(f"-{a1}-|-a2-|-a3-|-a4-\n -b1-|-b2-|-b3-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")

a2 = int(input("Enter number for cell a2:"))
print(f"-{a1}-|-{a2}-|-a3-|-a4-\n -b1-|-b2-|-b3-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
a3 = int(input("Enter number for cell a3:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-a4-\n -b1-|-b2-|-b3-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
a4 = int(input("Enter number for cell a4:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -b1-|-b2-|-b3-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
b1 = int(input("Enter number for cell b1:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-b2-|-b3-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
b2 = int(input("Enter number for cell b2:"))
print(f"-{a1}-|-a2-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-b3-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
b3 = int(input("Enter number for cell b3:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-b4-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
b4 = int(input("Enter number for cell b4:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -c1-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
c1 = int(input("Enter number for cell c1:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-c2-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
c2 = int(input("Enter number for cell c2:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-c3-|-c4-\n-d1-|-d2-|-d3-|-d4-")
c3 = int(input("Enter number for cell c3:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-{c3}-|-c4-\n-d1-|-d2-|-d3-|-d4-")
c4 = int(input("Enter number for cell c4:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-{c3}-|-{c4}-\n-d1-|-d2-|-d3-|-d4-")
d1 = int(input("Enter number for cell d1:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-{c3}-|-{c4}-\n-{d1}-|-d2-|-d3-|-d4-")
d2 = int(input("Enter number for cell d2:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-{c3}-|-{c4}-\n-{d1}-|-{d2}-|-d3-|-d4-")
d3 = int(input("Enter number for cell d3:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-{c3}-|-{c4}-\n-{d1}-|-{d2}-|-{d3}-|-d4-")
d4 = int(input("Enter number for cell d4:"))
print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-{c3}-|-{c4}-\n-{d1}-|-{d2}-|-{d3}-|-{d4}-")
## render into a matrix

print(f"-{a1}-|-{a2}-|-{a3}-|-{a4}-\n -{b1}-|-{b2}-|-{b3}-|-{b4}-\n -{c1}-|-{c2}-|-{c3}-|-{c4}-\n-{d1}-|-{d2}-|-{d3}-|-{d4}-")
challenge = input("Is this the correct form? y/n:")
if challenge == "y":
    print("accepted")
else:
      print("GO BACKKKK")



matrix_row = [[a1, a2, a3, a4] [b1, b2, b3, b4] [c1, c2, c3, c4] [d1, d2, d3, d4]]
matrix_column = [[a1, b1, c1, d1] [a2, b2, c2, d2] [a3, b3, c3, d3] [a4, b4, c4, d4]]
## find the minimum of each row


## subtract the minimum value from all values in the residential row

#PHASE 2

# find the minimum value of each column

## subtract the minimum value from all values in the residential column

#PHASE 3

#LAY OUT LINES ON THE ZEROS EITHER HORIZONTAL OR VERTICAL
# IF THE MINIMUM NUMBER OF LINES IS NOT EQUALS TO THE DIMENTION OF MATIX

