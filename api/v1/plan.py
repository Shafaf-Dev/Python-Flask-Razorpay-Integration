from flask import jsonify, request
from flask.views import MethodView

from . import v1
# from model.subscription import Plan
from extension import db

# test v1 api endpoint.
class Plan(MethodView):
    def get(self):
        return jsonify({"test": "This is plan api"}), 200
    
    def post(self):
        req :dict = request.get_json()
        username = req.get("name")
        if username is None:
            return jsonify({"message": "name is required"}), 400
        
        email = req.get("email")
        if email is None:
            return jsonify({"message": "email is required"}), 400
        # user = Plan(
        #     username=username,
        #     email=email
        # )
        
        print("start")
        print(username)
        print(email)
        print("end")
        
        # db.session.add(user)
        # db.session.commit()
        
        print(user.id)
        
        return jsonify({"status": True})

v1.add_url_rule("/plan", view_func=Plan.as_view("plan"))