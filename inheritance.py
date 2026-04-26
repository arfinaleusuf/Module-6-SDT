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
    
class Phone:
    def __init__(self, dual_sim):
 
        self.dual_sim = dual_sim
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with {text}'

class Camera:
    def __init__(self,pixel):
        self.pixel = pixel
    def change_lens(self):
        pass
    

