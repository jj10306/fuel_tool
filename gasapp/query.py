from gasapp import db
from gasapp.models import Vehicle


class Query:
    def __init__(self, id):
        self.id = id

    def get_gas(self):
        vehicle = db.session.query(Vehicle).distinct().filter_by(id = self.id).first()
        return (vehicle.fuel_type, vehicle.mpg)
