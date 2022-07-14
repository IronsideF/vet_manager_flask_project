from db.run_sql import run_sql
from models import *
import repositories.vet_repository as vet_repo
# INDEX
# GET /animals
def select_all():
    results = run_sql("SELECT * FROM animals")
    animals = []
    for row in results:
        vet = vet_repo.select(row['vet_id'])
        animal = Animal(row['name'], row['dob'], row['type'], row['owner_details'], row['treatment_notes'], vet, row['id'])
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
        animal = Animal(result['name'], result['dob'], result['type'], result['owner_details'], result['treatment_notes'], vet, result['id'])
    return animal

# CREATE
# POST /animals
def save(animal):
    result = run_sql("INSERT INTO animals (name, dob, type, owner_details, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", [animal.name, animal.dob, animal.type, animal.owner_details, animal.treatment_notes, animal.vet.id])[0]
    animal.id = result['id']
    return animal


# UPDATE
# POST /animals/<id>

# DELETE
# POST /animals/<id>/delete
def delete(id):
    run_sql("DELETE FROM animals WHERE id = %s", [id])

def delete_all():
    run_sql('DELETE FROM animals')