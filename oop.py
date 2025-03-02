#oop-modules-pip

# object-oriented-p 
# nesne-yönelimli-programlama

class Car():  # nesne KALIBI
    # constructor - yapıcı method
    def __init__(self, model, year=2025):
        self.__model = model
        self.year = year
        print("Car nesnesi oluşturuldu")

    def start(self, a): #self -> classın kendisi
        print(f"{self.__model} {a} arabası çalıştırılıyor.")
        self.startEngine()
    
    def startEngine(self):
        print("Motor başlatılıyor")
    
    def set_model(self,model):
        if len(model) < 3:
            print("Model ismi min. 3 hane olmalıdır.")
            return
        self.__model = model
    def get_model(self): 
        return self.__model
#read-only
#write-only

car1 = Car("Toyota") # car1 => Car instance'ı 
#print(car1.__model) # get-set
car1.set_model("ab")
print(car1.get_model())
car1.start(1)

car2 = Car("Hyundai", 2020) # Car classının yapıcı methodu
car2.start(2)