# Euclid's algorithm to find gcd of two numbers

def gcd (a,b):
    if b>a:
        (a,b) = (b,a)
    while (b!=0):
        temp = a
        a = b
        b = temp % b
    return a

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
print (gcd(a,b))


    