a = int(input('enter num1 : '))
b = int(input('enter num2 : '))
print(" type 1 for add\n type 2 for subtract\n type 3 for multiply\n type 4 for divide\n type 5 for exit")
option = input('enter your option : ').lower().strip()

# option.lower().strip()
# option = option.lower()
# option = option.strip()

while option != "exit":
    if option == "add":
        result = a + b
        print("add : ", result)
        print(" type 1 for add\n type 2 for subtract\n type 3 for multiply\n type 4 for divide\n type 5 for exit")
        option = input('enter your option : ').lower().strip()
        a = int(input('enter num1 : '))
        b = int(input('enter num2 : '))
    elif option == "sub":
        result = a - b
        print("sub : ", result)
        print(" type 1 for add\n type 2 for subtract\n type 3 for multiply\n type 4 for divide\n type 5 for exit")
        option = input('enter your option : ').lower().strip()
        a = int(input('enter num1 : '))
        b = int(input('enter num2 : '))
    elif option == "mul":
        result = a * b
        print("multiply : ", result)
        print(" type 1 for add\n type 2 for subtract\n type 3 for multiply\n type 4 for divide\n type 5 for exit")
        option = input('enter your option : ').lower().strip()
        a = int(input('enter num1 : '))
        b = int(input('enter num2 : '))
    elif option == "div":
        result = a / b
        print("divide : ", result)
        print(" type 1 for add\n type 2 for subtract\n type 3 for multiply\n type 4 for divide\n type 5 for exit")
        option = input('enter your option : ').lower().strip()
        a = int(input('enter num1 : '))
        b = int(input('enter num2 : '))
    elif option == "exit":
        continue
    else:
        print('invalid code')
        break


