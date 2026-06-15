from app import db

class Job(db.Model):
    __tablename__ = 'jobs'

    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String(200), nullable=False)
    company      = db.Column(db.String(150), nullable=False)
    location     = db.Column(db.String(150))
    job_type     = db.Column(db.String(50))   # full-time, part-time, internship
    description  = db.Column(db.Text, nullable=False)
    tags         = db.Column(db.String(300))  # e.g. "python,flask,sql"
    salary       = db.Column(db.String(100))
    is_active    = db.Column(db.Boolean, default=True)
    posted_at    = db.Column(db.DateTime, default=db.func.now())
    recruiter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    applications = db.relationship('Application', backref='job', lazy=True)