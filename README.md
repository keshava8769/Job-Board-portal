# 🚀 Job Board Portal

A full-stack web application built with Python Flask — a mini version of LinkedIn/Indeed where recruiters can post jobs and students can search and apply.

---

## 📸 Preview

> A platform with two user roles — **Recruiters** who post and manage jobs, and **Students** who search, filter, and apply with resume uploads.

---

## ✨ Features

- 🔐 **User Authentication** — Signup, login, logout with hashed passwords (Bcrypt)
- 👥 **Role-Based Access** — Separate flows for Students and Recruiters
- 📋 **Job Listings** — Recruiters can post jobs with title, description, location, type, salary, and tags
- 🔍 **Job Search & Filters** — Filter by keyword, location, and job type
- 📄 **Resume Upload** — Students upload PDF/Word resumes when applying (max 5MB)
- 📊 **Recruiter Dashboard** — View all applicants, download resumes, update application status
- 📁 **Application Tracker** — Students can track status of all their applications (Pending / Reviewed / Accepted / Rejected)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| ORM | Flask-SQLAlchemy |
| Database | SQLite (development) / PostgreSQL (production) |
| Auth | Flask-Login, Flask-Bcrypt |
| Frontend | HTML5, Bootstrap 5, Jinja2 |
| File Handling | Werkzeug |
| Server | Gunicorn (production) |

---

## 📁 Project Structure

```
job_board/
├── app/
│   ├── __init__.py          ← App factory
│   ├── models/
│   │   ├── user.py          ← User model (student / recruiter)
│   │   ├── job.py           ← Job listing model
│   │   └── application.py   ← Job application model
│   ├── routes/
│   │   ├── auth.py          ← Login, signup, logout
│   │   ├── jobs.py          ← Post, list, search, delete jobs
│   │   └── applications.py  ← Apply, dashboard, status update
│   ├── static/
│   │   ├── css/style.css
│   │   └── resumes/         ← Uploaded resumes stored here
│   └── templates/
│       ├── base.html
│       ├── auth/            ← login.html, signup.html
│       ├── jobs/            ← list.html, detail.html, post.html
│       └── dashboard/       ← student.html, recruiter.html
├── config.py
├── run.py
├── requirements.txt
└── .env
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/job-board-portal.git
cd job-board-portal
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root folder

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///jobboard.db
```

### 5. Run the application

```bash
python run.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 🗄️ Database Models

### User
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| name | String | Full name |
| email | String | Unique email |
| password | String | Bcrypt hashed |
| role | String | `student` or `recruiter` |

### Job
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| title | String | Job title |
| company | String | Company name |
| location | String | City or Remote |
| job_type | String | full-time / part-time / internship |
| description | Text | Full job description |
| tags | String | Comma-separated skills |
| salary | String | Salary range |
| recruiter_id | FK → users | Posted by |

### Application
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| resume_filename | String | Uploaded file name |
| cover_letter | Text | Optional message |
| status | String | pending / reviewed / accepted / rejected |
| student_id | FK → users | Applied by |
| job_id | FK → jobs | Applied to |

---

## 🔗 URL Routes

| URL | Method | Description |
|---|---|---|
| `/` | GET | Redirects to job listings |
| `/auth/signup` | GET, POST | Register new account |
| `/auth/login` | GET, POST | Login |
| `/auth/logout` | GET | Logout |
| `/jobs/` | GET | Browse and search jobs |
| `/jobs/<id>` | GET | View job detail |
| `/jobs/post` | GET, POST | Post a new job (recruiter) |
| `/jobs/delete/<id>` | GET | Remove a job listing |
| `/apply/<job_id>` | POST | Submit application (student) |
| `/apply/my-applications` | GET | View own applications (student) |
| `/apply/recruiter-dashboard` | GET | View applicants (recruiter) |
| `/apply/update-status/<id>` | POST | Update application status |

---

## 🚀 Deployment

This app is ready to deploy on [Render](https://render.com).

1. Push code to GitHub
2. Create a PostgreSQL database on Render
3. Create a Web Service connected to your GitHub repo
4. Set environment variables: `SECRET_KEY` and `DATABASE_URL`
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn run:app`

---

## 🔒 Security Features

- Passwords hashed with **Bcrypt** — never stored in plain text
- File uploads validated by **extension whitelist** (PDF, DOC, DOCX only)
- Filenames sanitized with **werkzeug secure_filename**
- Max upload size enforced (**5MB limit**)
- Role checks on every sensitive route
- `@login_required` decorator protecting all authenticated pages

---

## 📌 Future Improvements

- [ ] Email notifications when application status changes
- [ ] Cloud storage for resumes (AWS S3 / Cloudinary)
- [ ] Pagination on job listings
- [ ] Job bookmarking for students
- [ ] Admin panel for platform management
- [ ] REST API for mobile app support

---

## 👨‍💻 Author

**Chenna Keshava**  
Python Full-Stack Developer  
📧 bairu.chennakeshava05@gmail.com  
🔗 [GitHub](https://github.com/keshava8769)  
🔗 [LinkedIn]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/bairu-chenna-keshava/))

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
