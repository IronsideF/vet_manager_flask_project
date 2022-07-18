from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *
from datetime import date, time, datetime

appoints_blueprint = Blueprint('appoints', __name__)

# INDEX
# GET /appointments
@appoints_blueprint.route('/appointments')
def index():
    appointments = appoint_repo.select_all()
    return render_template('appointments/index.html', appointments=appointments, date=date.today())

# SHOW
# GET /appointments/<id>
@appoints_blueprint.route('/appointments/<id>')
def show(id):
    appointment=appoint_repo.select(id)
    treatments = appoint_repo.treatments(id)
    existing_treatment_names = []
    for treatment in treatments:
        existing_treatment_names.append(treatment.name)
    all_treatments = treatment_repo.select_all()
    possible_treatments = [treatment for treatment in all_treatments if treatment.name not in existing_treatment_names]
    return render_template('appointments/show.html', appointment=appointment, date=date.today(), treatments=treatments, possible_treatments=possible_treatments)

# NEW
# GET /appointments/new
@appoints_blueprint.route('/appointments/<id>/new')
def new(id):
    animal = animal_repo.select(id)
    vets=vet_repo.select_all()
    return render_template('appointments/new.html', date=date.today(), patient=animal, vets=vets)

# CREATE
# POST /appointments
@appoints_blueprint.route('/appointments', methods=['POST'])
def create():
    vet=vet_repo.select(request.form['vet_id'])
    patient=animal_repo.select(request.form['patient_id'])
    appointment=Appointment(request.form['date'], request.form['time'], patient, vet)
    appoint_repo.save(appointment)
    return redirect(f'/appointments/{appointment.id}')

# EDIT
# GET /appointments/<id>/edit
@appoints_blueprint.route('/appointments/<id>/edit')
def edit(id):
    appointment = appoint_repo.select(id)
    patient = appointment.patient
    vets = vet_repo.select_all()
    return render_template('appointments/edit.html', appointment=appointment, date=date.today(), patient=patient, vets=vets)


# UPDATE
# POST /appointments/<id>
@appoints_blueprint.route('/appointments/<id>', methods=['POST'])
def update(id):
    vet=vet_repo.select(request.form['vet_id'])
    patient=animal_repo.select(request.form['patient_id'])
    appointment=Appointment(request.form['date'], request.form['time'], patient, vet, id)
    appoint_repo.update(appointment)
    return redirect(f'/appointments/{appointment.id}')

# DELETE
# POST /appointments/<id>/delete
@appoints_blueprint.route('/appointments/<id>/delete', methods=['POST'])
def delete(id):
    appoint_repo.delete(id)
    return redirect('/appointments')

@appoints_blueprint.route('/appointments/<id>/add-treatment', methods=['POST'])
def add_treatment(id):
    appointment = appoint_repo.select(id)
    at_repo.save(id, request.form['treatment_id'])
    return redirect(f'/appointments/{appointment.id}')
