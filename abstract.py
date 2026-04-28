class Animal:
    def eat(self):
        print('eating banana')
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self):
        self.name = 'Monkey'
        super().__init__()


layka = Monkey('lucky')
layka.eat()