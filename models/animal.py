from datetime import date, time, datetime, timedelta

class Animal:
    def __init__(self, _name, _age, _type, _owner, _vet, _check_in=None, _check_out=None, _id=None):
        self.name = _name
        self.age = _age
        self.type = _type
        self.owner = _owner
        self.vet = _vet
        self.check_in = _check_in
        self.check_out = _check_out
        self.id = _id