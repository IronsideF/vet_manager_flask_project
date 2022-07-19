from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *
from datetime import date, time, datetime

animals_blueprint = Blueprint('animals', __name__)

# INDEX
# GET /animals
@animals_blueprint.route('/animals')
def index():
    animals=animal_repo.select_all()
    return render_template('animals/index.html', animals=animals, date=date.today())

# SHOW
# GET /animals/<id>
@animals_blueprint.route('/animals/<id>')
def show(id):
    animal = animal_repo.select(id)
    appointments = animal_repo.appointments(id)
    return render_template('animals/show.html', animal=animal, date=date.today(), appointments=appointments)

# NEW
# GET /animals/new
@animals_blueprint.route('/animals/<id>/new')
def new(id):
    vets = vet_repo.select_all()
    owner = owner_repo.select(id)
    return render_template('animals/new.html', vets=vets, owner=owner, date=date.today())

# CREATE
# POST /animals
@animals_blueprint.route('/animals', methods=['POST'])
def create():
    vet = vet_repo.select(request.form['vet_id'])
    owner = owner_repo.select(request.form['owner_id'])
    animal = Animal(request.form['name'], request.form['age'], request.form['type'], owner, request.form['treatment_notes'], vet)
    animal = animal_repo.save(animal)
    return redirect(f'/animals/{animal.id}')


# EDIT
# GET /animals/<id>/edit
@animals_blueprint.route('/animals/<id>/edit')
def edit(id):
    animal = animal_repo.select(id)
    vets = vet_repo.select_all()
    owners = owner_repo.registered_only()
    return render_template('animals/edit.html', animal=animal, vets=vets, owners=owners, date=date.today())

# UPDATE
# POST /animals/<id>
@animals_blueprint.route('/animals/<id>', methods=['POST'])
def update(id):
    vet = vet_repo.select(request.form['vet_id'])
    owner = owner_repo.select(request.form['owner_id'])
    animal = Animal(request.form['name'], request.form['age'], request.form['type'], owner, request.form['treatment_notes'], vet, id)
    animal_repo.update(animal)
    return redirect(f'/animals/{animal.id}')

# DELETE
# POST /animals/<id>/delete
@animals_blueprint.route('/animals/<id>/delete', methods=['POST'])
def delete(id):
    animal_repo.delete(id)
    return redirect('/animals')

@animals_blueprint.route('/animals/<id>/checkin', methods=['POST'])
def check_in(id):
    animal = animal_repo.select(id)
    animal.check_in = request.form['check_in']
    animal.check_out = request.form['check_out']
    animal_repo.update(animal)
    return redirect(f'/animals/{animal.id}')

