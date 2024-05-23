from flask import jsonify, request
from flask.views import MethodView

from . import v1
from model.subscription import Plan
from extension import db, client


class Plans(MethodView):
    def get(self):
        plans = Plan.query.all()
        plans_data = [
            {
                "id": plan.id,
                "name": plan.name,
                "period" : plan.period,
                "currency" : plan.currency,
                "description": plan.description,
                "amount": plan.amount,
                "intervals": plan.intervals,
                "plan_id": plan.plan_id,
                "notes" : plan.notes
            }
            for plan in plans
        ]
        
        return jsonify(plans_data), 200
    
    def post(self):
        req :dict = request.get_json()
        
        plan_name = req.get("name")
        plan_amount = req.get("amount")
        plan_interval = req.get("interval")
        plan_period = req.get("period")
        currency = req.get("currency")
        
        if plan_name is None:
            return jsonify({"message": "name is required"}), 400
        
        if plan_amount is None:
            return jsonify({"message": "amount is required"}), 400
          
        if plan_interval is None:
            return jsonify({"message": "interval is required"}), 400
    

        try:
            plan = client.plan.create({
                "period": plan_period,
                "interval": plan_interval,
                "item": {
                    "name": plan_name,
                    "amount": plan_amount,
                    "currency": currency,
                    "description": req.get("description")
                },
                "notes": req.get("notes")
            })
            
            plan = Plan(
                name=plan_name,
                period=plan_period,
                currency=currency,
                description=req.get("description"),
                amount=plan_amount,
                intervals=plan_interval,
                plan_id=plan["id"],
                notes=req.get("notes")
            )
            
            db.session.add(plan)
            db.session.commit()    
            
            return jsonify({"id": plan.id}), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

v1.add_url_rule("/plan", view_func=Plans.as_view("plan"))