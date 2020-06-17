from sqlalchemy import Column

from app.config import app_db


class Measurement(app_db.Model):
    __tablename__ = 'measurements'

    id = Column(app_db.Integer, primary_key=True)
    date = Column(app_db.DateTime, nullable=False)
    category = Column(app_db.String(250), nullable=False)
    value = Column(app_db.Integer, nullable=False)
    sensor_id = Column(app_db.Integer, nullable=False)
    control_point_id = Column(app_db.Integer, nullable=False)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
