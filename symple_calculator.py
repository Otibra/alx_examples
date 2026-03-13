def calculator():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    op = input('Enter your operator (+, -, *, /, %, **): ')

    if op == '+':
        print('Result =', num1 + num2)

    elif op == '-':
        print('Result =', num1 - num2)

    elif op == '*':
        print('Result =', num1 * num2)

    elif op == '/':
        if num2 != 0:
            print('Result =', num1 / num2)
        else:
            print('Invalid division (cannot divide by zero)')

    elif op == '**':
        print('Result =', num1 ** num2)

    elif op == '%':
        if num2 != 0:
            print('Result =', num1 % num2)
        else:
            print('Invalid modulo (cannot divide by zero)')

    else:
        print('Invalid operator')

calculator()
