from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *

vets_blueprint = Blueprint('vets', __name__)

# INDEX
# GET /vets
@vets_blueprint.route('/vets')
def index():
    vets = vet_repo.select_all()
    return render_template('vets/index.html', vets=vets)

# SHOW
# GET /vets/<id>
@vets_blueprint.route('/vets/<id>')
def show(id):
    vet = vet_repo.select(id)
    animals = vet_repo.animals(vet)
    return render_template('vets/show.html', vet=vet, animals=animals)

# NEW
# GET /vets/new
@vets_blueprint.route('/vets/new')
def new():
    return render_template('vets/new.html')

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
    return render_template('vets/edit.html', vet=vet)

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