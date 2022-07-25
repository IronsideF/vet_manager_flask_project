# vet_manager_flask_project
Welcome to the Toby's Angels Vet Manager App. I was given a brief as follows:
The practice wants to:
    be able to register / track animals. Important information for the vets to know is -
        Name
        Date Of Birth (use a VARCHAR initially)
        Type of animal
        Contact details for the owner
        Treatment notes
    Be able to assign animals to vets
    CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?

This app will allow you do do this and more. You can register animals, vets and owners and create appointments for them. You can add treatments to your practice and add them to appointments, use those appointments to calculate bills for owners and more!

It was created using Python3, HTML5, CSS, Postgres, Psycopg2, Flask 

To get it running, you'll need to download this repo and follow a few steps. Ensure you have all the neccessary programs installed:
    1. Create the database - ```createdb vet_manager```
    2. Set up your tables. In the main folder, run this ```psql -d vet_manager -f db/vet_manager.sql```
    3. In the main folder, start the app with ```flask run```

And you're good to go!
