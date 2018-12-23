'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320'''

number = int(input("Enter the number to compute the factorial : "))
i = 1
fact = 1
while i <= number:
       if number == 0:
              fact = 1
              break
       else:
              fact = fact * i
       i += 1
print(fact)
       
