from cProfile import run
from models import *
from db.run_sql import run_sql
import repositories.vet_repository as vet_repo
import repositories.animal_repository as animal_repo

# INDEX
# GET /appointments
def select_all():
    appointments = []
    results = run_sql("SELECT * FROM appointments ORDER BY date")
    for row in results:
        vet = vet_repo.select(row['vet_id'])
        animal = animal_repo.select(row['patient_id'])
        appointment = Appointment(row['date'], row['time'], animal, vet, row['id'])
        appointments.append(appointment)
    return appointments

# SHOW
# GET /appointments/<id>
def select(id):
    appointment = None
    results = run_sql("SELECT * FROM appointments WHERE id = %s", [id])
    if results:
        result = results[0]
        vet=vet_repo.select(result['vet_id'])
        animal = animal_repo.select(result['patient_id'])
        appointment = Appointment(result['date'], result['time'], animal, vet, result['id'])
    return appointment

# CREATE
# POST /appointments
def save(appointment):
    result = run_sql("INSERT INTO appointments (date, time, patient_id, vet_id) VALUES (%s, %s, %s, %s) RETURNING *", [appointment.date, appointment.time, appointment.patient.id, appointment.vet.id])[0]
    appointment.id = result['id']
    return appointment

# UPDATE
# POST /appointments/<id>
def update(appointment):
    run_sql("UPDATE appointments SET (date, time, patient_id, vet_id) = (%s, %s, %s, %s) WHERE id = %s", [appointment.date, appointment.time, appointment.patient.id, appointment.vet.id, appointment.id])

# DELETE
# POST /appointments/<id>/delete
def delete(id):
    run_sql("DELETE FROM appointments WHERE id = %s", [id])

def delete_all():
    run_sql("DELETE FROM appointments")
