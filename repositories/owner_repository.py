from db.run_sql import run_sql
from models import *
import repositories.vet_repository as vet_repo
import repositories.animal_repository as animal_repo

# INDEX
# GET /owners
def select_all():
    owners = []
    results = run_sql("SELECT * FROM owners ORDER BY last_name")
    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['phone_num'], row['email'], row['address'], row['registered'], row['id'])
        owners.append(owner)
    return owners

# SHOW
# GET /owners/<id>
def select(id):
    owner = None
    results = run_sql("SELECT * FROM owners WHERE id = %s", [id])
    if results:
        result = results[0]
        owner=Owner(result['first_name'], result['last_name'], result['phone_num'], result['email'], result['address'], result['registered'], result['id'])
    return owner

# CREATE
# POST /owners
def save(owner):
    result = run_sql("INSERT INTO owners (first_name, last_name, phone_num, email, address, registered) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", [owner.first_name, owner.last_name, owner.phone_num, owner.email, owner.address, owner.registered])[0]
    owner.id = result['id']
    return owner

# UPDATE
# POST /owners/<id>
def update(owner):
    run_sql("UPDATE owners SET (first_name, last_name, phone_num, email, address, registered) = (%s, %s, %s, %s, %s, %s) WHERE id = %s", [owner.first_name, owner.last_name, owner.phone_num, owner.email, owner.address, owner.registered, owner.id])

# DELETE
# POST /vets/<id>/delete
def delete(id):
    run_sql("DELETE FROM owners WHERE id = %s", [id])

# DELETE ALL
def delete_all():
    run_sql("DELETE FROM owners")

# ANIMALS
def animals(owner):
    results = run_sql("SELECT * FROM animals WHERE owner_id = %s ORDER BY name", [owner.id])
    animals=[]
    if results:
        for row in results:
            vet = vet_repo.select(row['vet_id'])
            animal = Animal(row['name'], row['dob'], row['type'], owner, row['treatment_notes'], vet, row['id'])
            animals.append(animal)
    return animals

# SHOW ONLY REGISTERED
def registered_only():
    results = run_sql("SELECT * FROM owners WHERE registered = true ORDER BY last_name")
    owners = []
    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['phone_num'], row['email'], row['address'], row['registered'], row['id'])
        owners.append(owner)
    return owners

