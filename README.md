# University Project, Thesis and Industrial Training Management System

A web-based management system for handling university projects, thesis, and industrial training activities.

## Features

- User Authentication
- Student Management
- Supervisor Management
- Project Submission
- Thesis Management
- Industrial Training Management
- Progress Report Submission
- Viva Scheduling
- Evaluation & Marks Management
- Notice Management

---

## Technologies Used

### Backend
- Python
- Django
- Django REST Framework
- SQLite

### Frontend
- HTML
- CSS
- Tailwind CSS
- JavaScript

### Version Control
- Git
- GitHub

---

# Project Setup Guide

## Step 1: Clone Repository

```bash
git clone https://github.com/waliullah9277/universityProjectAndThesisManagement.git
```

---

## Step 2: Move Into Project Folder

```bash
cd universityProjectAndThesisManagement
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 6: Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

Example:

Username:
admin

Email:
admin@gmail.com

Password:
********

---

## Step 8: Run Development Server

```bash
python manage.py runserver
```

---

## Access Project

Application:

```text
http://127.0.0.1:8000/
```

Admin Panel:

```text
http://127.0.0.1:8000/admin/
```

---

## Installed Django Apps

- accounts
- projects
- reports
- viva
- notices

---

## Current Development Status

### Completed

- Django Project Setup
- GitHub Repository Setup
- Django REST Framework Setup
- Application Structure Creation

### In Progress

- User Authentication Module
- Project Submission Module
- Progress Report Module
- Viva Scheduling Module

---

## Author

Waliullah

Department of Computer Science and Engineering

Green University of Bangladesh
