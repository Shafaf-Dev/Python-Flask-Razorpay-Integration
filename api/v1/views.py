from flask import jsonify
from flask.views import MethodView

from . import v1

# test v1 api endpoint.
class Live(MethodView):
    def get(self):
        return jsonify({"Live": True, "version": "v0.0.1"}), 200
    
v1.add_url_rule("", view_func=Live.as_view("live"))
