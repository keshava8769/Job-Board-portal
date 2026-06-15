from app import db

class Application(db.Model):
    __tablename__ = 'applications'

    id              = db.Column(db.Integer, primary_key=True)
    resume_filename = db.Column(db.String(300), nullable=False)
    cover_letter    = db.Column(db.Text)
    status          = db.Column(db.String(50), default='pending')
    applied_at      = db.Column(db.DateTime, default=db.func.now())
    student_id      = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id          = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)