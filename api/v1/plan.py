from flask import jsonify
from flask.views import MethodView

from . import v1

# test v1 api endpoint.
class Plan(MethodView):
    def get(self):
        return jsonify({"test": "This is plan api"}), 200

v1.add_url_rule("/plan", view_func=Plan.as_view("plan"))