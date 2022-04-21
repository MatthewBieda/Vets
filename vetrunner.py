from vets import *

#Object instantiation 
cat1 = Cat("Allie", 10, "White")
print(cat1.eat())

dog1 = Dog("Rex", 7, "Red")
print(dog1.grow())
print(dog1.die())

Goldie = AFish("Goldfish", "Golden", "Pacific Ocean")
print(Goldie.move())
print(Goldie.eat())
print(f"Fish 1 lives in the {Goldie.region}")
print(Goldie.jump())

Birdie = Bird("7cm", "North Carolina", "Black", "Blackbird")
print(Birdie.grow())
print(Birdie.name)

animal_list = [cat1, dog1, Goldie, Birdie]
print((animal_list[0].name))
