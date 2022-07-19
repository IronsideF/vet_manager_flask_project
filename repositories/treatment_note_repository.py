from models import *
from datetime import date, time
import repositories.vet_repository as vet_repo
import repositories.animal_repository as animal_repo
from db.run_sql import run_sql

def delete_all():
    run_sql("DELETE FROM treatment_notes")

def delete(id):
    run_sql("DELETE FROM treatment_notes WHERE id = %s", [id])

def save(treatment_note):
    result = run_sql("INSERT INTO treatment_notes (date, time, body, animal_id, vet_id) VALUES(%s, %s, %s, %s, %s) RETURNING *", [treatment_note.date, treatment_note.time, treatment_note.body, treatment_note.animal.id, treatment_note.vet.id])[0]
    treatment_note.id=result['id']
    return treatment_note

def update(treatment_note):
    run_sql("UPDATE treatment_notes SET body = %s WHERE id = %s", [treatment_note.body, treatment_note.id])