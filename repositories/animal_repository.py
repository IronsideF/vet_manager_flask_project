from db.run_sql import run_sql
from models import *
import repositories.vet_repository as vet_repo
import repositories.owner_repository as owner_repo
import repositories.appointment_repository as appoint_repo
from datetime import date, timedelta
# INDEX
# GET /animals
def select_all():
    results = run_sql("SELECT animals.*, owners.last_name FROM animals INNER JOIN owners ON owners.id = animals.owner_id ORDER BY owners.last_name")
    animals = []
    for row in results:
        vet = vet_repo.select(row['vet_id'])
        owner = owner_repo.select(row['owner_id'])
        age = (date.today() - row['dob']) // timedelta(365)
        animal = Animal(row['name'], age, row['type'], owner, vet, row['check_in'], row['check_out'], row['id'])
        animals.append(animal)
    return animals


# SHOW
# GET /animals/<id>
def select(id):
    results = run_sql("SELECT * FROM animals WHERE id = %s", [id])
    animal = None
    if results:
        result = results[0]
        vet = vet_repo.select(result['vet_id'])
        owner = owner_repo.select(result['owner_id'])
        age = (date.today() - result['dob']) // timedelta(365)
        animal = Animal(result['name'], age, result['type'], owner, vet, result['check_in'], result['check_out'], result['id'])
    return animal

# CREATE
# POST /animals
def save(animal):
    dob = date(date.today().year - int(animal.age), date.today().month, date.today().day)
    result = run_sql("INSERT INTO animals (name, dob, type, owner_id, vet_id, check_in, check_out) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *", [animal.name, dob, animal.type, animal.owner.id, animal.vet.id, animal.check_in, animal.check_out])[0]
    animal.id = result['id']
    return animal


# UPDATE
# POST /animals/<id>
def update(animal):
    run_sql("UPDATE animals SET (name, type, owner_id, vet_id, check_in, check_out) = (%s, %s, %s, %s, %s, %s) WHERE id = %s", [animal.name, animal.type, animal.owner.id, animal.vet.id, animal.check_in, animal.check_out, animal.id])


# DELETE
# POST /animals/<id>/delete
def delete(id):
    run_sql("DELETE FROM animals WHERE id = %s", [id])

def delete_all():
    run_sql('DELETE FROM animals')

def select_animals_in_practice():
    animals =[]
    results = select_all()
    today = date.today()
    for animal in results:
        if animal.check_in and animal.check_out:
            if animal.check_in < today > animal.check_out:
                animals.append(animal)
    return animals

def appointments(id):
    appointments =[]
    results = run_sql("SELECT * FROM appointments WHERE patient_id = %s", [id])
    if results:
        for row in results:
            appointment = appoint_repo.select(row['id'])
            appointments.append(appointment)
    return appointments

def t_notes(id):
    t_notes = []
    results = run_sql("SELECT * FROM treatment_notes WHERE animal_id = %s ORDER BY date DESC", [id])
    if results:
        for row in results:
            animal = select(id)
            vet = vet_repo.select(row['vet_id'])
            tn = TreatmentNote(row['date'], row['time'], row['body'], animal, vet, row['id'])
            t_notes.append(tn)
    return t_notes

        

