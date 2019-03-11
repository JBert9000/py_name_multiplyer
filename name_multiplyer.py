import time

name_input = input('Type in your name: ')
print_number = int(input('How many times would you like to repeat your name? '))

for x in range(print_number):
    print(name_input)

time.sleep(5)
