from flask import Flask, render_template, redirect, Blueprint, request
from models import *
from repositories import *

owners_blueprint = Blueprint('owners', __name__)