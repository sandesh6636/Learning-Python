class Car:
    def __init__(self,brand,model):
        self.__brand= brand
        self.model= model
    
    def fule_type(self):
        return "Petrol and Deseal"
    def get_Ful_details(self):
        return f"Name {self.__brand} Model {self.model}"

class ElectricCar (Car):
    def __init__(self,brand, model,battry_capacity):
        super().__init__(brand,model)
        self.battery_capacity= battry_capacity
    def fule_type(self):
        return "Battery"
    

my_Car = Car("Tesla","Model S")
print( my_Car.model)
print(my_Car.fule_type())
print(my_Car.get_Ful_details())
# new_car = ElectricCar("Tesla","Tesla S","400kwh")
# print(new_car.brand, new_car.battery_capacity)
# print(new_car.fule_type())