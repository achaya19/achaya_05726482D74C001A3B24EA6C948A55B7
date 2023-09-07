# Implement a recursive function to calculate the factorial of a givien number. 
"""
1! = 1 A-1
2! = 2 A-1!
3! = 3 A-2!
.
.
10! = 10 A-9!

Formula - n A-(n-1)!
"""

def fact_rec(n):
 if n==0 or n==1:
   return 1
 else :
   return n*fact_rec(n-1)

number = int(input("enter a value :"))
res = fact_rec(number)
print("The factorial of{} is {}".format(number,res))