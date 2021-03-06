class Owner:
    def __init__(self, _f_name, _l_name, _phone_num, _email, _address, _registered=True, _debt=0, _id=None):
        self.first_name=_f_name
        self.last_name=_l_name
        self.phone_num=_phone_num
        self.email=_email
        self.address=_address
        self.registered=_registered
        self.debt = _debt
        self.id=_id

    def registration(self):
        self.registered = not self.registered

    def debt_change(self, amount):
        self.debt += amount