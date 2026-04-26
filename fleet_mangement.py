# ena porubahon

class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisers = []
        self.fare = []

class Drivers:
    def __init__(self, name, license, age) -> None:
        self.license = license
        self.name = name
        self.age = age
class Counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self,start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

red_mia = Drivers('a',123,32)
