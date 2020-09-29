# Given a range of first 10 numbers, Iterate 
# from start number to the end number and 
# print the sum of the current number 
# and previous number

for i in range (1,10):
    sum = i + (i-1)
    print (" current number {} + previous number {} = {}" .format(i, i-1, sum))
    


 
