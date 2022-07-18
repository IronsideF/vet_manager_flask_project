from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *
from datetime import date, time, datetime

treatments_blueprint = Blueprint('treatments', __name__)
# INDEX
# GET /appointments

# SHOW
# GET /appointments/<id>

# NEW

# CREATE

# EDIT

# UPDATE

# DELETE