from db.run_sql import run_sql
from models import *
# INDEX
# GET /vets

# SHOW
# GET /vets/<id>

# NEW
# GET /vets/new

# CREATE
# POST /vets
def save(vet):
    result = run_sql("INSERT INTO vets (first_name, last_name, specialism) VALUES (%s, %s, %s) RETURNING *", [vet.first_name, vet.last_name, vet.specialism])[0]
    vet.id = result['id']
    return vet

# EDIT
# GET /vets/<id>/edit

# UPDATE
# POST /vets/<id>

# DELETE
# POST /vets/<id>/delete

def delete_all():
    run_sql('DELETE FROM vets')