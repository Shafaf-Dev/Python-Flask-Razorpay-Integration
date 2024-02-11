from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_utils import UUIDType
import os
import uuid

# SQLAlchemy.
pg_user = os.getenv("POSTGRES_USER", "postgres")
pg_pass = os.getenv("POSTGRES_PASSWORD", "postgres")
pg_host = os.getenv("POSTGRES_HOST", "postgres")
pg_port = os.getenv("POSTGRES_PORT", "5432")
pg_db = os.getenv("POSTGRES_DB", pg_user)

app = Flask(__name__, template_folder="./templates")

# db configuration
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{pg_user}:{pg_pass}@localhost:{pg_port}/{pg_db}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your-secret-key"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Base model class for all models
class BaseModel(db.Model):
    """
        Base model of the mapping class inheritace 

        https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    """

    __abstract__ = True

    STATUS_CHOICES = ["Active", "Disabled", "Deleted"]

    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    extra = db.Column(db.JSON(), nullable=True)
    status = db.Column(
        db.Enum(*STATUS_CHOICES, name="status", native_enum=False),
        nullable=False,
        default="active"
    )

# User Model
class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(520), nullable=False)


class Student(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(200), nullable=False)
    student_age = db.Column(db.Integer, nullable=True)
    student_course = db.Column(db.String(200), nullable=True)


# Routes
@app.route("/")
def index():
    return "Welcome you again"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash("Login successful", "success")
            # You can redirect to a dashboard or profile page here
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # check if the user is already registered
        existing_user = User.query.filter_by(username=username).first()
        print(existing_user)

        if existing_user:
            flash("User name already exist, Please choose another", "danger")
        else:
            # create a new user
            new_user = User(
                username=username,
                password=password,
                name=username,
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful. You can now log in.", "success")
            return redirect(url_for("login"))

    else:
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
