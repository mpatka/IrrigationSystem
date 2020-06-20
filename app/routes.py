import json
from datetime import datetime

import numpy as np
from flask import request, jsonify, render_template

from app.config import app_db
from app.ml_models import ml_model_loader
from app.models import Measurement


def init_routes(application):
    @application.route('/')
    def home():
        sensors = [1, 2, 3, 4, 5]

        return render_template('home_page.html', sensors=sensors)

    @application.route('/measurements', methods=['POST'])
    def send_measurement_data():
        data = request.get_json()
        if data is None:
            raise Exception('Incorrect payload')

        measurement = Measurement(date=datetime.now(), category=data['category'], value=data['value'],
                                  sensor_id=data['sensor_id'], control_point_id=data['control_point_id'])
        app_db.session.add(measurement)
        app_db.session.commit()

        return 'OK'

    @application.route('/measurements', methods=['GET'])
    def all_measurements():
        measurements = Measurement.query.all()
        result = [measurement.as_dict() for measurement in measurements]
        return jsonify(result)

    @application.route('/irrigation/<int:control_point_id>', methods=['GET'])
    def irrigation(control_point_id):
        model = ml_model_loader.load_newest('app/ml_models/')
        result = model.predict([[control_point_id]])

        class NumpyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, np.ndarray):
                    return obj.tolist()
                return json.JSONEncoder.default(self, obj)

        json_dump = json.dumps(result, cls=NumpyEncoder)
        return jsonify(json_dump)
