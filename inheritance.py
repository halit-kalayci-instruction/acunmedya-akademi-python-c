# Inheritance (Kalıtım,Miras)
class Vehicle():
    def __init__(self,model):
        self.model = model
    
    def start(self):
        print(f"{self.model} araç başlatılıyor")

class Car(Vehicle):
    def __init__(self,model):
        #self.model # car classı
        super().__init__(model) #super() fonksiyonu kalıtım aldığım classı ifade eder.

class Truck(Vehicle):
    def __init__(self,model):
        super().__init__(model)
    
    def start(self):
        print(f"{self.model} kamyoneti başlatılıyor.") #method overriding
        # polymorphism (ARAŞTIRMA)

class Motocyle(Vehicle):
    def __init__(self):
        pass

car1 = Car("Hyundai")
car1.start()

truck1 = Truck("Scania")
truck1.start()