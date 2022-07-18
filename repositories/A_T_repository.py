from models import *
from db.run_sql import run_sql

def save(appointment_id, treatment_id):
    run_sql("INSERT INTO AppointmentTreatments (appointment_id, treatment_id) VALUES (%s, %s)", [appointment_id, treatment_id])

def delete_all():
    run_sql("DELETE FROM AppointmentTreatments")
