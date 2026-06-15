from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(100), nullable=False)
    email        = db.Column(db.String(150), unique=True, nullable=False)
    password     = db.Column(db.String(200), nullable=False)
    role         = db.Column(db.String(20), nullable=False)  # 'student' or 'recruiter'
    created_at   = db.Column(db.DateTime, default=db.func.now())

    jobs_posted  = db.relationship('Job', backref='recruiter', lazy=True)
    applications = db.relationship('Application', backref='applicant', lazy=True)