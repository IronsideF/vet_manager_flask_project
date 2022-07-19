DROP TABLE IF EXISTS AppointmentTreatments;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS treatment_notes;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS treatments;


CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    specialism VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_num VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    registered BOOLEAN
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    type VARCHAR(255),
    owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    treatment_notes TEXT,
    vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE,
    check_in DATE,
    check_out DATE
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    date DATE,
    time TIME,
    patient_id INT REFERENCES animals(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    description TEXT,
    price INT
);

CREATE TABLE AppointmentTreatments (
    id SERIAL PRIMARY KEY,
    appointment_id INT REFERENCES appointments(id) ON DELETE CASCADE,
    treatment_id INT REFERENCES treatments(id) ON DELETE CASCADE
);

CREATE TABLE treatment_notes (
    id SERIAL PRIMARY KEY,
    date DATE,
    time TIME,
    body TEXT,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);