from flask import jsonify
from flask.views import MethodView

from . import v1

class Subscription(MethodView):
    def get(self):
        return jsonify({"value": "yes, test is working....:)"})
    
v1.add_url_rule("/subscription", view_func=Subscription.as_view("subscription"))
