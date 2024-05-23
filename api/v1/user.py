from flask import jsonify, request
from flask.views import MethodView

from . import v1
from model.subscription import User
from extension import db

class Users(MethodView):
    
    def get(self):
        users = User.query.all()
        user_obj = [
            {
                "id" : user.id,
                "name" : user.name,
                "email" : user.email,
                "phone_number" : user.phone_number   
            }
            for user in users
        ]
        return jsonify(user_obj), 200
    
    def post(self):
        req: dict = request.get_json()
        
        # check and validate user input.
        username = req.get("name")
        email = req.get("email")
        phone_number = req.get("phone_number")
        
        if not username:
            return jsonify({"message" : "name is required"}), 400
        
        if not email:
            return jsonify({"message" : "email is required"}), 400
        
        if not phone_number:
            return jsonify({"message" : "phone_number is required"}), 400
        
        user = User(
            name= username,
            email= email,
            phone_number=phone_number
        )
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({"id": user.id}), 201

v1.add_url_rule("/users", view_func=Users.as_view('user'))