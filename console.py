from models import *
from repositories import *


vet_repo.delete_all()
animal_repo.delete_all()

vet1 = Vet('James', 'Bond', 'Cat')
vet2 = Vet('Jack', 'Bauer', 'Dog')
vet3 = Vet('Ace', 'Ventura', 'Chinchilla')
vet_repo.save(vet1)
vet_repo.save(vet2)
vet_repo.save(vet3)

animal1 = Animal('Toby', '01/05/2021', 'Dog', 'Nathaniel Forsyth, 4 Hyde Park', 'Bad back leg, very needy', vet2)
animal2 = Animal('Tom', '06/09/1987', 'Cat', 'Clint Clobber, 71 Tweed Street', 'Obsessed with chasing', vet1)
animal3 = Animal('BuBu', '21/03/2012', 'Chinchilla', 'Clara Creek, The Old House on the Hill', 'Very cute, fame has gone to her head somewhat', vet3)
animal_repo.save(animal1)
animal_repo.save(animal2)
animal_repo.save(animal3)

# animal_repo.delete(animal3.id)
# vet_repo.delete(vet3.id)

# print(vet1.__dict__, animal1.__dict__)
animals = animal_repo.select_all()
vets = vet_repo.select_all()

tom = animal_repo.select(animal2.id)
jack = vet_repo.select(vet2.id)
# nobody = vet_repo.select(87)
# not_a_dog = animal_repo.select(99)

for animal in animals:
    print(animal.__dict__)

for vet in vets:
    print(vet.__dict__)

# print(tom.__dict__, jack.__dict__)
# print(nobody, not_a_dog)
