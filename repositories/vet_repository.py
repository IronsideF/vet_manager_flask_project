from db.run_sql import run_sql
from models import *
import repositories.owner_repository as owner_repo
# INDEX
# GET /vets
def select_all():
    vets = []
    results = run_sql("SELECT * FROM vets ORDER BY last_name")
    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['specialism'], row['id'])
        vets.append(vet)
    return vets

# SHOW
# GET /vets/<id>
def select(id):
    vet = None
    results = run_sql("SELECT * FROM vets WHERE id = %s", [id])
    if results:
        result=results[0]
        vet = Vet(result['first_name'], result['last_name'], result['specialism'], result['id'])
    return vet

# CREATE
# POST /vets
def save(vet):
    result = run_sql("INSERT INTO vets (first_name, last_name, specialism) VALUES (%s, %s, %s) RETURNING *", [vet.first_name, vet.last_name, vet.specialism])[0]
    vet.id = result['id']
    return vet

# UPDATE
# POST /vets/<id>
def update(vet):
    run_sql("UPDATE vets SET (first_name, last_name, specialism) = (%s, %s, %s) WHERE id = %s", [vet.first_name, vet.last_name, vet.specialism, vet.id])

# DELETE
# POST /vets/<id>/delete

def delete(id):
    run_sql("DELETE FROM vets WHERE id = %s", [id])

def delete_all():
    run_sql('DELETE FROM vets')

def animals(vet):
    results = run_sql("SELECT * FROM animals WHERE vet_id = %s ORDER BY id", [vet.id])
    animals=[]
    if results:
        for row in results:
            owner = owner_repo.select(row['owner_id'])
            animal = Animal(row['name'], row['dob'], row['type'], row['owner_details'], row['treatment_notes'], vet, row['id'])
            animals.append(animal)
    return animals