from flask import Flask, render_template
from controllers import *
from datetime import date, time, datetime
import calendar
from repositories import *

app = Flask(__name__)

app.register_blueprint(animals_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(appoints_blueprint)
app.register_blueprint(treatments_blueprint)
app.register_blueprint(tn_blueprint)

today=date.today()
our_calendar=calendar.HTMLCalendar()
this_month = our_calendar.formatmonth(theyear=today.year, themonth=today.month)

@app.route('/')
def index():
    return render_template('index.html', date=date.today(), calendar=this_month, animals_in_practice=animal_repo.select_animals_in_practice())

if __name__ == "__main__":
    app.run(debug=True)