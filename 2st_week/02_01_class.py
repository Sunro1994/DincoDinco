
class Person:
    def __init__(self, name):
        self.name = name
        print("hihi" ,self.name)

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다")


person_1 = Person('유재석')
print(person_1.name)
person_1.talk()
person_2 = Person('박명수')
print(person_2.name)
person_2.talk()