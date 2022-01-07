class Calculator(object):
    def addition(self, a, b):
        return a + b

    def substraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def value_input(self, a, b, _input):
        if _input == 'add' :
            return self.addition(a, b)
        if _input == 'sub':
            return self.substraction(a, b)
        if _input == 'mul':
            return self.multiplication(a, b)
        if _input == 'div':
            return self.division(a, b)
        if _input == 'exit':
            return None


print("type add to add 2 nos.")
print("type sub to subtract 2 nos.")
print("type mul to multiply 2 nos.")
print ("type div to divide 2 nos.")
print("type exit to terminate program")
result = 1
c = Calculator()
while result:
    option = input("enter ur option: ")
    if option == 'exit':
        print('The program is terminated.')
        break
    a = int(input("enter no1: "))
    b = int(input("enter no2: "))
    result = c.value_input(a, b, option)
    print(result)






