from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from extension import db

class Plan(db.Model):
    __tablename__ = "plan"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String(300), nullable=True)
    amount = Column(Integer, nullable=False)
    intervals = Column(Integer, nullable=False)
    plan_id = Column(String)
    
class Subscription(db.Model):
    __tablename__ = "subscription"
    
    STATUS_CHOICES = ["active", "disabled"]
    
    id = Column(Integer, primary_key=True, nullable=False)
    plan_id = Column(Integer, ForeignKey(Plan.id), nullable=False)
    razorpay_user_id = Column(String)
    subscription_id = Column(String)
    subscription_status = Column(
        Enum(*STATUS_CHOICES, name="status", native_enum=False),
        nullable=False,
        default="active",
    )
    

class User(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    
