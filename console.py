from datetime import date, datetime, time
from models import *
from repositories import *

appoint_repo.delete_all()
vet_repo.delete_all()
animal_repo.delete_all()
owner_repo.delete_all()
treatment_repo.delete_all()

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

treatment1 = Treatment('Neutering', 'The Chop', 75)
treatment2 = Treatment('Stitches', 'Sewing it up', 50)
treatment3 = Treatment('Consultation', 'Coming in for a chat', 45)
treatment_repo.save(treatment1)
treatment_repo.save(treatment2)
treatment_repo.save(treatment3)

appointment1=Appointment(date(2022, 8, 15), time(9, 45), animal2, vet1)
appointment2=Appointment(date(2022, 9, 25), time(10, 30), animal3, vet3)
appointment3=Appointment(date(2022, 7, 25), time(13, 00), animal1, vet2)
appoint_repo.save(appointment1)
appoint_repo.save(appointment2)
appoint_repo.save(appointment3)

# treatment1.description = 'Slicing'
# appointment1.date=date(2022, 9, 15)
# treatment_repo.update(treatment1)
# appoint_repo.update(appointment1)

# stitch = treatment_repo.select(treatment2.id)
# toby_time = appoint_repo.select(appointment3.id)
# treatment_repo.delete(treatment3.id)
# appoint_repo.delete(appointment2.id)


animals = animal_repo.select_all()
vets = vet_repo.select_all()
owners = owner_repo.select_all()
appointments = appoint_repo.select_all()
treatments = treatment_repo.select_all()

# tom = animal_repo.select(animal2.id)
# jack = vet_repo.select(vet2.id)
# nobody = vet_repo.select(87)
# not_a_dog = animal_repo.select(99)


# for animal in animals:
#     print(animal.__dict__)

# for vet in vets:
#     print(vet.__dict__)

# for owner in owners:
#     print(owner.__dict__)

# for treatment in treatments:
#     print(treatment.__dict__)

# for appointment in appointments:
#     print(appointment.__dict__)

# print(stitch.__dict__, toby_time.__dict__)

# print(tom.__dict__, jack.__dict__)
# print(nobody, not_a_dog)
