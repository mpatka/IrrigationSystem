from datetime import datetime

from flask import request, jsonify

from app.config import app_db
from app.models import Measurement


def init_routes(application):
    @application.route('/')
    def home():
        return "Home page"

    @application.route('/measurement', methods=['POST'])
    def send_measurement_data():
        data = request.get_json()
        if data is None:
            raise Exception('Incorrect payload')

        measurement = Measurement(date=datetime.now(), category=data['category'], value=data['value'],
                                  sensor_id=data['sensor_id'], control_point_id=data['control_point_id'])
        app_db.session.add(measurement)
        app_db.session.commit()

        return 'OK'

    @application.route('/measurement', methods=['GET'])
    def all_measurements():
        measurements = Measurement.query.all()
        result = [measurement.as_dict() for measurement in measurements]
        return jsonify(result)
