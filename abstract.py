from abc import ABC, abstractmethod
#  abstract base class

class Animal(ABC):
    @abstractmethod  #enforce all derived class to have a eat mathord
    def eat(self):
        print(' I name food')
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name):
        self.catagory = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('Hey na nana')


layka = Monkey('lucky')
layka.eat()