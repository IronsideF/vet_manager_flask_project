from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *

animals_blueprint = Blueprint('animals', __name__)

# INDEX
# GET /animals

# SHOW
# GET /animals/<id>

# NEW
# GET /animals/new

# CREATE
# POST /animals

# EDIT
# GET /animals/<id>/edit

# UPDATE
# POST /animals/<id>

# DELETE
# POST /animals/<id>/delete