
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"{self.model} charged to {self.battery}%."

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"



class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)
        self.strap_color = strap_color

    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"{self.model} smartwatch now at {self.battery}% battery."

    def track_steps(self, steps):
        return f"{self.model} tracked {steps} steps today!"


phone = Smartphone("Samsung", "Galaxy S25", 512)
watch = Smartwatch("Apple", "Watch Series 9", 50, "White")

print(phone.make_call("254-795-280-444"))
print(watch.charge(30))
print(watch.track_steps(5000))



#ACTIVITY 2

class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def move(self):
        return "Running"

class Bird(Animal):
    def move(self):
        return "Flying"

class Fish(Animal):
    def move(self):
        return "Swimming"


animals = [Dog(), Bird(), Fish()]

for a in animals:
    print(a.move())
