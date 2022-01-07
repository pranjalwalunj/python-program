# class Calculator(object):
#
#     def add(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
#
#     def mul(self, a, b):
#         return a * b
#
#     def div(self, a, b):
#         return a // b
#
#     def exit(self):
#         return
#
#     def handle_input(self, a, b, _input):
#         if _input == 'add':
#             return self.add(a, b)
#         if _input == 'sub':
#             return self.sub(a, b)
#         if _input == 'div':
#             return self.div(a, b)
#         if _input == 'mul':
#             return self.mul(a, b)
#
#
# if __name__ == '__main__':
#     print("Type 'add' to add these two numbers")
#     print("Type 'sub' to subtract these two numbers")
#     print("Type 'mul' to multiply these two numbers")
#     print("Type 'div' to divide these two numbers")
#     print("Type 'exit' to exit the program")
#     result = 1
#     c = Calculator()
#     while result:
#         option = input('enter your option : ').lower().strip()
#         if option == 'exit':
#             break
#         a = int(input('enter num1 : '))
#         b = int(input('enter num2 : '))
#         result = c.handle_input(a, b, option)
#         print(result)
#
