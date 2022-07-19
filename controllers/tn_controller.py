from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *
from datetime import date, time, datetime

tn_blueprint = Blueprint('treatment_notes', __name__)

@tn_blueprint.route('/tnotes', methods=['POST'])
def create():
    animal = animal_repo.select(request.form['animal_id'])
    vet = vet_repo.select(request.form['vet_id'])
    now = datetime.today()
    tn = TreatmentNote(date.today(), time(now.hour, now.minute), request.form['body'], animal, vet)
    tn_repo.save(tn)
    return redirect(f'/animals/{animal.id}')

@tn_blueprint.route('/tnotes/<id>/<animal_id>/delete', methods=['POST'])
def delete(id, animal_id):
    tn_repo.delete(id)
    return redirect(f'/animals/{animal_id}')