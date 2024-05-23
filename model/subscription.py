from sqlalchemy import Column, String, Integer, ForeignKey, Enum, JSON
from sqlalchemy.orm import Mapped, mapped_column
from extension import db

class Plan(db.Model):
    __tablename__ = "plan"
    PERIOD_CHOICES = ["daily", "weekly", "monthly", "yearly"]
    
    id = Column(Integer, primary_key=True, nullable=False)
    period = Column(
        Enum(*PERIOD_CHOICES, name="period_types", native_enum=False),
        nullable=False,
        default="monthly"
    )
    currency = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String(300), nullable=True)
    amount = Column(Integer, nullable=False)
    intervals = Column(Integer, nullable=False)
    plan_id = Column(String)
    notes = Column(JSON, nullable=False)
    
class Subscription(db.Model):
    __tablename__ = "subscription"
    
    STATUS_CHOICES = ["active", "disabled"]
    
    id = Column(Integer, primary_key=True, nullable=False)
    plan_id = Column(Integer, ForeignKey(Plan.id), nullable=False)
    total_count = Column(Integer, nullable=False)
    razorpay_user_id = Column(String)
    subscription_id = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    notes = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=True)
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
    
