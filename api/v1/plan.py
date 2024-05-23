from flask import jsonify, request
from flask.views import MethodView

from . import v1
from model.subscription import Plan

from extension import db

class Plans(MethodView):
    def get(self):
        plans = Plan.query.all()
        plans_data = [
            {
                "id": plan.id,
                "name": plan.name,
                "description": plan.description,
                "amount": plan.amount,
                "intervals": plan.intervals,
                "plan_id": plan.plan_id
            }
            for plan in plans
        ]
        
        return jsonify(plans_data), 200
    
    def post(self):
        req :dict = request.get_json()
        
        plan_name = req.get("name")
        plan_amount = req.get("amount")
        plan_interval = req.get("interval")
        
        if plan_name is None:
            return jsonify({"message": "name is required"}), 400
        
        if plan_amount is None:
            return jsonify({"message": "amount is required"}), 400
          
        if plan_interval is None:
            return jsonify({"message": "interval is required"}), 400
        
        plan = Plan(
            name=plan_name,
            description=req.get("description"),
            amount=plan_amount,
            intervals=plan_interval,
            plan_id=req.get("plan_id")
        )
        
        db.session.add(plan)
        db.session.commit()    
        
        return jsonify({"id": plan.id})

v1.add_url_rule("/plan", view_func=Plans.as_view("plan"))