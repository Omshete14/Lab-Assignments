"""
Python program for determining whether a traingle is Right-Angled or not
"""

a = int(input("Enter First Side:"))
b = int(input("Enter Second Side:"))
c = int(input("Enter Third Side:"))

if a*a + b*b == c*c:
    print("It's a Right Angled Triangle")

elif b*b + c*c == a*a:
    print("It's a Right Angled Triangle")

elif c*c + a*a == b*b:
    print("It's a Right Angled Triangle")

else:
    print("Triangle is not Right Angled")