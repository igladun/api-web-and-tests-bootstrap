from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(40))
    birthdate = db.Column(db.String(40)) #todo finish with DateTime
    address = db.Column(db.String(120))

    def __init__(self, name, email, birthdate, address):
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.address = address

    def json(self):
        return {'name': self.name,
                'email': self.email,
                'birthdate': self.birthdate,
                'address': self.address, }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
