class Animal:
    def __init__(self, _name, _dob, _type, _owner_details, _treatment_notes, _vet, _id=None):
        self.name = _name
        self.dob = _dob
        self.type = _type
        self.owner_details = _owner_details
        self.treatment_notes = _treatment_notes
        self.vet = _vet
        self.id = _id