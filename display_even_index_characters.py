

'''
Given a string, display only those characters
which are present at an even index number.

'''

input_string = input ("Enter the string \n")

for i in range(0, len(input_string), 2):
   print ("[",i,"]", input_string[i])
   