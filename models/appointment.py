class Appointment:
    def __init__(self, _date, _time, _patient, _vet, _id=None):
        self.date = _date
        self.time = _time
        self.patient=_patient
        self.vet=_vet
        self.id=_id