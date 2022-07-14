DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    specialism VARCHAR
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    dob VARCHAR,
    type VARCHAR,
    owner_details VARCHAR,
    treatment_notes VARCHAR,
    vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
);