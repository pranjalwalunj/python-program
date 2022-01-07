
EYES = 2


class Animal(object):

    def __init__(self, legs, hands, sound):
        self.legs = legs
        self.hands = hands
        self.sound = sound

    def animal_sound(self, sound):
        return f'{sound}'

    def who_am_i(self):
        sentence = "I am an animal"
        return sentence

    def get_details(self):
        return f'I have {self.legs} legs and {self.hands} hands' \
               f'and I {self.sound}. Obviously I only have {EYES} eyes'


dog = Animal(4, 0, 'bark')
print( dog.get_details())



# a = Animal(2, 3, 4)

# class Human(object):
#
#     def __init__(self, name, age, hobbies):
#         self.name = name
#         self.age = age
#         self.hobbies = hobbies
#
#     def details(self):
#         return f'I am {self.name}, my age is {self.age}'
#
#     def _hobbies(self):
#         s = ""
#         for hobby in self.hobbies:
#             s += hobby + ", "
#         return s


# pranjal = Human('Pranjal', 20, ['running', 'dancing'])
#
# hobbies = pranjal._hobbies()
# print(type(hobbies))