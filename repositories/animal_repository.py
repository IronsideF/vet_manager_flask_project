from db.run_sql import run_sql
from models import *

# INDEX
# GET /animals



# SHOW
# GET /animals/<id>

# NEW
# GET /animals/new

# CREATE
# POST /animals
def save(animal):
    result = run_sql("INSERT INTO animals (name, dob, type, owner_details, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", [animal.name, animal.dob, animal.type, animal.owner_details, animal.treatment_notes, animal.vet.id])[0]
    animal.id = result['id']
    return animal

# EDIT
# GET /animals/<id>/edit

# UPDATE
# POST /animals/<id>

# DELETE
# POST /animals/<id>/delete

def delete_all():
    run_sql('DELETE FROM animals')