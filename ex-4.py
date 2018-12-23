'''Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

sequence = input("Please enter a sequence of numbers - ")
number_list = []
for each in (sequence.split(',')):
       number_list.append(each)

number_tuple = tuple(sequence.split(','))


print(number_list)
print(number_tuple)
