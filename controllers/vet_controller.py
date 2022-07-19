from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *
from datetime import date, time, datetime

vets_blueprint = Blueprint('vets', __name__)

# INDEX
# GET /vets
@vets_blueprint.route('/vets')
def index():
    vets = vet_repo.select_all()
    return render_template('vets/index.html', vets=vets, date=date.today())

# SHOW
# GET /vets/<id>
@vets_blueprint.route('/vets/<id>')
def show(id):
    vet = vet_repo.select(id)
    animals = vet_repo.animals(vet)
    appointments = vet_repo.appointments(id)
    t_notes = vet_repo.t_notes(id)
    return render_template('vets/show.html', vet=vet, animals=animals, appointments=appointments, date=date.today(), t_notes=t_notes)

# NEW
# GET /vets/new
@vets_blueprint.route('/vets/new')
def new():
    return render_template('vets/new.html', date=date.today())

# CREATE
# POST /vets
@vets_blueprint.route('/vets', methods=['POST'])
def create():
    vet = Vet(request.form['first_name'], request.form['last_name'], request.form['specialism'])
    vet=vet_repo.save(vet)
    return redirect (f'/vets/{vet.id}')

# EDIT
# GET /vets/<id>/edit
@vets_blueprint.route('/vets/<id>/edit')
def edit(id):
    vet=vet_repo.select(id)
    return render_template('vets/edit.html', vet=vet, date=date.today())

# UPDATE
# POST /vets/<id>
@vets_blueprint.route('/vets/<id>', methods=['POST'])
def update(id):
    vet = Vet(request.form['first_name'], request.form['last_name'], request.form['specialism'], id)
    vet_repo.update(vet)
    return redirect (f'/vets/{vet.id}')


# DELETE
# POST /vets/<id>/delete
@vets_blueprint.route('/vets/<id>/delete', methods=['POST'])
def delete(id):
    vet_repo.delete(id)
    return redirect ('/vets')