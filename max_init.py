# User puts in a number, find the highest number from the user until he puts in a negative number

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int=0
num_int=int(input('Input a value: '))
while num_int >= 0:
    num_int=int(input('Input a value: '))
    if num_int > max_int:
        max_int=num_int

print("The maximum is", max_int)    # Do not change this line
