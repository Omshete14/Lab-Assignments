"""
PYTHON CODE FOR LARGEST OF THREE NUMBERS
"""

a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter Third number:"))

if a>b and a>c:
    print(a,"is the largest number")

elif b>a and b>c:
    print(b,("is the largest number"))

elif c>a and c>b:
    print(c,("is the largest number"))

