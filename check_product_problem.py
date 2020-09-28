# Given a two integer numbers return their product 
# and  if the product is greater than 1000, 
# then return their sum

print ("Enter the 1st number")
number_1 = int(input ())
print ("Enter the 2nd number")
number_2 = int (input ())

product = number_1 * number_2
sum_of_numbers = number_1 + number_2
if (product > 1000):
    print ("The result is sum ={}" .format(sum_of_numbers))
else:
    print ("product = {}".format(product))
