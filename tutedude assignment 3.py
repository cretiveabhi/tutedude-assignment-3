# task 1 : calculating factorial of the number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("enter a number:"))
fac=(factorial(n))
print("factorial of ",n," is ",fac)

# task 2 : using math module for calculations
import math
n=int (input("enter a number:"))
print("square root:",math.sqrt(n))
print("logarithm:",math.log(n))
print("sine:",math.sin(n))
