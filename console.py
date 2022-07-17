from models import *
from repositories import *


vet_repo.delete_all()
animal_repo.delete_all()
owner_repo.delete_all()

vet1 = Vet('James', 'Bond', 'Cat')
vet2 = Vet('Jack', 'Bauer', 'Dog')
vet3 = Vet('Ace', 'Ventura', 'Chinchilla')
vet_repo.save(vet1)
vet_repo.save(vet2)
vet_repo.save(vet3)

owner1 = Owner('Rachel', 'Stewart', '07724789582', 'rachel@stewart.com', '4 Hyde Park')
owner2 = Owner('Clint', 'Clobber', '00909073604', 'clobber@clobber.com', '71 Tweed Street')
owner3 = Owner('Clara', 'Creek', '07741238961', 'creek123@gmail.com', 'The Old House on the Hill')
owner1.registration()
owner1.registration()
owner_repo.save(owner1)
owner_repo.save(owner2)
owner_repo.save(owner3)

animal1 = Animal('Toby', 5, 'Dog', owner1, 'Bad back leg, very needy', vet2)
animal2 = Animal('Tom', 17, 'Cat', owner2, 'Obsessed with chasing', vet1)
animal3 = Animal('BuBu', 10, 'Chinchilla', owner3, 'Very cute, fame has gone to her head somewhat', vet3)
animal_repo.save(animal1)
animal_repo.save(animal2)
animal_repo.save(animal3)

# animal_repo.delete(animal3.id)
# vet_repo.delete(vet3.id)

# print(vet1.__dict__, animal1.__dict__)
# vet2.first_name = 'Finley'
# animal2.type = 'Mouse'
# vet_repo.update(vet2)
# animal_repo.update(animal2)
animals = animal_repo.select_all()
vets = vet_repo.select_all()
owners = owner_repo.select_all()

# tom = animal_repo.select(animal2.id)
# jack = vet_repo.select(vet2.id)
# nobody = vet_repo.select(87)
# not_a_dog = animal_repo.select(99)


for animal in animals:
    print(animal.__dict__)

for vet in vets:
    print(vet.__dict__)

for owner in owners:
    print(owner.__dict__)

# print(tom.__dict__, jack.__dict__)
# print(nobody, not_a_dog)
