from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *

owners_blueprint = Blueprint('owners', __name__)

# INDEX
# GET /owners
@owners_blueprint.route('/owners')
def index():
    owners = owner_repo.select_all()
    return render_template('owners/index.html', owners=owners)

# SHOW
# GET /owners/<id>
@owners_blueprint.route('/owners/<id>')
def show(id):
    owner = owner_repo.select(id)
    animals = owner_repo.animals(owner)
    return render_template('owners/show.html', owner=owner, animals=animals)

# NEW
# GET /owners/new
@owners_blueprint.route('/owners/new')
def new():
    return render_template('owners/new.html')

# CREATE
# POST /owners
@owners_blueprint.route('/owners', methods=['POST'])
def create():
    owner = Owner(request.form['first_name'], request.form['last_name'], request.form['phone_num'], request.form['email'], request.form['address'])
    owner = owner_repo.save(owner)
    return redirect (f'/owners/{owner.id}')
# EDIT
# GET /owners/<id>/edit
@owners_blueprint.route('/owners/<id>/edit')
def edit(id):
    owner = owner_repo.select(id)
    return render_template('owners/edit.html', owner=owner)

# UPDATE
# POST /owners/<id>
def update(id):
    owner = Owner(request.form['first_name'], request.form['last_name'], request.form['phone_num'], request.form['email'], request.form['address'], request.form['registered'], id)
    owner_repo.update(owner)
    return redirect(f'/owners/{owner.id}')

# DELETE
# POST /owners/<id>/delete
@owners_blueprint.route('/owners/<id>/delete')
def delete(id):
    owner_repo.delete(id)
    return redirect ('/owners')