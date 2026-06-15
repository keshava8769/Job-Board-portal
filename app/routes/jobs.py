from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.job import Job

jobs = Blueprint('jobs', __name__)

@jobs.route('/')
def list_jobs():
    search   = request.args.get('search', '')
    job_type = request.args.get('type', '')
    location = request.args.get('location', '')

    query = Job.query.filter_by(is_active=True)

    if search:
        query = query.filter(
            Job.title.ilike(f'%{search}%') |
            Job.tags.ilike(f'%{search}%') |
            Job.company.ilike(f'%{search}%')
        )
    if job_type:
        query = query.filter_by(job_type=job_type)
    if location:
        query = query.filter(Job.location.ilike(f'%{location}%'))

    all_jobs = query.order_by(Job.posted_at.desc()).all()
    return render_template('jobs/list.html', jobs=all_jobs)


@jobs.route('/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('jobs/detail.html', job=job)


@jobs.route('/post', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.role != 'recruiter':
        flash('Only recruiters can post jobs.', 'danger')
        return redirect(url_for('jobs.list_jobs'))

    if request.method == 'POST':
        job = Job(
            title        = request.form['title'],
            company      = request.form['company'],
            location     = request.form['location'],
            job_type     = request.form['job_type'],
            description  = request.form['description'],
            tags         = request.form['tags'],
            salary       = request.form['salary'],
            recruiter_id = current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!', 'success')
        return redirect(url_for('jobs.list_jobs'))

    return render_template('jobs/post.html')


@jobs.route('/delete/<int:job_id>')
@login_required
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    if job.recruiter_id != current_user.id:
        flash('Unauthorized.', 'danger')
        return redirect(url_for('jobs.list_jobs'))
    job.is_active = False
    db.session.commit()
    flash('Job removed.', 'info')
    return redirect(url_for('jobs.list_jobs'))