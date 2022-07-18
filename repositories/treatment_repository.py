from models import *
from db.run_sql import run_sql
import repositories.appointment_repository as appoint_repo

# INDEX
# GET /treatments
def select_all():
    treatments = []
    results = run_sql("SELECT * FROM treatments ORDER BY name")
    for row in results:
        treatment = Treatment(row['name'], row['description'], row['price'], row['id'])
        treatments.append(treatment)
    return treatments

# SHOW
# GET /treatements/<id>
def select(id):
    treatment = None
    results = run_sql("SELECT * FROM treatments WHERE id = %s", [id])
    if results:
        result = results[0]
        treatment = Treatment(result['name'], result['description'], result['price'], result['id'])
    return treatment

# CREATE
# POST /treatments
def save(treatment):
    result = run_sql("INSERT INTO treatments (name, description, price) VALUES (%s, %s, %s) RETURNING *", [treatment.name, treatment.description, treatment.price])[0]
    treatment.id=result['id']
    return treatment
    

# UPDATE
# POST /treatments/<id>
def update(treatment):
    result = run_sql("UPDATE treatments SET (name, description, price) = (%s, %s, %s) WHERE id=%s", [treatment.name, treatment.description, treatment.price, treatment.id])

# DELETE
# POST /treatments/<id>/delete
def delete(id):
    run_sql("DELETE FROM treatments WHERE id = %s", [id])

def delete_all():
    run_sql("DELETE FROM treatments")

def appointments(id):
    results = run_sql("SELECT appointment_id FROM AppointmentTreatments WHERE treatment_id = %s", [id])
    appointments =[]
    for row in results:
        appointment = appoint_repo.select(row['appointment_id'])
        appointments.append(appointment)
    return appointments
