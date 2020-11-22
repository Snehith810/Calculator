# Taking inputs.
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another numeber: '))
operator = input('Enter an operator: ')

# Creating a default variable called result.
result = ''

# Using a for loop "if elif" to make calculator.
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
elif operator == '%':
    result = num1 % num2
else:
    result = 'error'

# Now print the result.
if result == 'error':
    print('Invalid Operator!')
else:
    print('Your result is '+str(result)+'.')
