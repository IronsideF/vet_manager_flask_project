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
day_of_the_week = today.weekday()
days_of_week = ['Monday!', 'Tuesday!', 'Wednesday!', 'Thursday!', 'Friday!', 'Saturday!', 'Sunday!']
stringed_day = days_of_week[day_of_the_week]

@app.route('/')
def index():
    return render_template('index.html', date=date.today(), calendar=this_month, appointments_today=appoint_repo.select_by_day(date.today()), day=stringed_day)

if __name__ == "__main__":
    app.run(debug=True)