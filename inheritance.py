#  base class , parent class, commom attribute + functional class
#  derived class, child class, uncommon attribite + functionality class

class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    def run(self):
        return f'running laptop {self.brand}'

class Leptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd
  
    def coding(self):
        return f'learning python and practicing'
    
class Phone(Gadget):
    def __init__(self, dual_sim, brand, color,price, origin):
        self.dual_sim = dual_sim
        super().__init__(brand, price,color, origin)

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with {text}'
    def __repr__(self) -> str:
        return f'Phone: {self.brand} {self.price} {self.dual_sim}'

class Camera:
    def __init__(self,pixel):
        self.pixel = pixel
    def change_lens(self):
        pass
    

#  inheritance
my_phone = Phone(True,'iphone','silver',120000, 'china')
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)