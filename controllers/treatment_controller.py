from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *
from datetime import date, time, datetime

treatments_blueprint = Blueprint('treatments', __name__)
# INDEX
# GET /treatments
@treatments_blueprint.route('/treatments')
def index():
    treatments = treatment_repo.select_all()
    return render_template('treatments/index.html', treatments=treatments, date=date.today())

# SHOW
# GET /treatments/<id>
@treatments_blueprint.route('/treatments/<id>')
def show(id):
    treatment = treatment_repo.select(id)
    return render_template('treatments/show.html', treatment=treatment, date=date.today())

# NEW
# GET /treatments/new
@treatments_blueprint.route('/treatments/new')
def new():
    return render_template('treatments/new.html', date=date.today())

# CREATE
# POST /treatments
@treatments_blueprint.route('/treatments', methods=['POST'])
def create():
    treatment = Treatment(request.form['name'], request.form['description'], request.form['price'])
    treatment_repo.save(treatment)
    return redirect('/treatments')

# EDIT
# GET /treatments/<id>/edit
@treatments_blueprint.route('/treatments/<id>/edit')
def edit(id):
    treatment = treatment_repo.select(id)
    return render_template('treatments/edit.html', treatment=treatment, date=date.today())

# UPDATE
# POST /treatments/<id>
@treatments_blueprint.route('/treatments/<id>', methods=['POST'])
def update(id):
    treatment = Treatment(request.form['name'], request.form['description'], request.form['price'], id)
    treatment_repo.update(treatment)
    return redirect('/treatments')

# DELETE
# POST /treatments/<id>/delete
@treatments_blueprint.route('/treatments/<id>/delete', methods=['POST'])
def delete(id):
    treatment_repo.delete(id)
    return redirect('/treatments')
