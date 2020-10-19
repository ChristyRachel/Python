'''
Created on Oct. 18, 2020

@author: christy

Odd even test hacker rank P1

'''

n = int(input())
rem = n % 2
if (rem) != 0:
    print("Weird")
else:
    if (1<n<7):
        print("Not Weird")
    elif (5<n<21):
        print("Weird")
    else:
        print("Not Weird")