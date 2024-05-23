from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import razorpay

from connection import RAZORPAY_KEY_ID, RAZORPAY_SECRET

db = SQLAlchemy()
migrate = Migrate()
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET))