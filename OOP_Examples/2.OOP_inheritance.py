class Animal: 
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
        def __repr__(self):
            return f"{self.name} is a {self.species}"
        
    def make_sound(Self, sound):
        print(f"this animal says {sound}!")
        
class Cat(Animal):
    
    def __init__(self, name, breed, toy):
        #super refers to paretn class
        super().__init__(name, species = "cat")
        self.breed = breed
        self.toy = toy
    

blue = Cat("Blue", "Cat", "Scottish Fold", "String")

print(blue.species)
print(blue.breed)
print(blue.toy)
blue.make_sound("meow")