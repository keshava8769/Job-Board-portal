import os
from flask import Blueprint, redirect, url_for, flash, request, current_app, render_template
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.models.application import Application
from app.models.job import Job

applications = Blueprint('applications', __name__)

ALLOWED = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED


@applications.route('/<int:job_id>', methods=['POST'])
@login_required
def apply(job_id):
    if current_user.role != 'student':
        flash('Only students can apply.', 'danger')
        return redirect(url_for('jobs.job_detail', job_id=job_id))

    already = Application.query.filter_by(
        student_id=current_user.id, job_id=job_id
    ).first()
    if already:
        flash('You already applied to this job.', 'warning')
        return redirect(url_for('jobs.job_detail', job_id=job_id))

    file = request.files.get('resume')
    if not file or not allowed_file(file.filename):
        flash('Please upload a PDF or Word document.', 'danger')
        return redirect(url_for('jobs.job_detail', job_id=job_id))

    filename = secure_filename(f"user{current_user.id}_job{job_id}_{file.filename}")
    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    new_app = Application(
        resume_filename = filename,
        cover_letter    = request.form.get('cover_letter', ''),
        student_id      = current_user.id,
        job_id          = job_id
    )
    db.session.add(new_app)
    db.session.commit()
    flash('Application submitted successfully!', 'success')
    return redirect(url_for('jobs.job_detail', job_id=job_id))


@applications.route('/my-applications')
@login_required
def my_applications():
    apps = Application.query.filter_by(student_id=current_user.id).all()
    return render_template('dashboard/student.html', applications=apps)


@applications.route('/recruiter-dashboard')
@login_required
def recruiter_dashboard():
    if current_user.role != 'recruiter':
        return redirect(url_for('jobs.list_jobs'))
    my_jobs = Job.query.filter_by(recruiter_id=current_user.id, is_active=True).all()
    return render_template('dashboard/recruiter.html', jobs=my_jobs)

@applications.route('/update-status/<int:app_id>', methods=['POST'])
@login_required
def update_status(app_id):
    if current_user.role != 'recruiter':
        flash('Unauthorized.', 'danger')
        return redirect(url_for('jobs.list_jobs'))

    application = Application.query.get_or_404(app_id)
    new_status = request.form.get('status')

    if new_status in ['pending', 'reviewed', 'accepted', 'rejected']:
        application.status = new_status
        db.session.commit()
        flash(f'Application status updated to {new_status}.', 'success')

    return redirect(url_for('applications.recruiter_dashboard'))