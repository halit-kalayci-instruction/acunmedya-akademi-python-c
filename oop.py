#oop-modules-pip

# object-oriented-p 
# nesne-yönelimli-programlama

class Car():  # nesne KALIBI
    model = ""

    # constructor - yapıcı method
    def __init__(self, model):
        self.model = model
        print("Car nesnesi oluşturuldu")

    def start(self, a): #self -> classın kendisi
        print(f"{self.model} {a} arabası çalıştırılıyor.")
        self.startEngine()
    
    def startEngine(self):
        print("Motor başlatılıyor")

car1 = Car("Toyota") # car1 => Car instance'ı 
car1.start(1)

car2 = Car("Hyundai") # Car classının yapıcı methodu
car2.start(2)