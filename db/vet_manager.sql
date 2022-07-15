DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

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
    dob VARCHAR(255),
    type VARCHAR(255),
    owner INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    treatment_notes TEXT,
    vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
);