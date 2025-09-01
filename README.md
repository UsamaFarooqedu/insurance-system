**Insurance Management System**


A Django-based backend for managing health insurance and social protection schemes. This project handles beneficiaries, policies, and claims, leveraging Python OOP principles, efficient data structures and algorithms (DSA), Django ORM, and Django REST Framework (DRF) for a scalable, secure API-driven system.

**Table of Contents**
Project Overview
Technologies
Folder Structure
Setup Instructions
API Endpoints
My Contributions

**Project Overview**
The Insurance Management System is a modular backend application designed to manage:

Beneficiaries: Registration and lookup of insured individuals.
Policies: Creation and management of insurance policies linked to beneficiaries.
Claims: Submission and prioritized processing of insurance claims.
This project demonstrates a robust implementation of a real-world insurance system, with a focus on maintainability, scalability, and security.

**Technologies**
Python: Object-oriented programming for model design.
Django: ORM, views, and URL routing for backend logic.
Django REST Framework: RESTful APIs with serializers, authentication, and pagination.
MySQL: Relational database for data persistence.
DSA: Hash tables for O(1) lookups, priority queues for efficient claim/policy processing.
Folder Structure

**insurance_system/**
├── manage.py
├── insurance_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── beneficiaries/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
├── policies/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
├── claims/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
└── README.md

**Setup Instructions**
To run the project locally, follow these steps:

Clone the repository (replace <your-repo-url> with the actual URL if hosted):

git clone <your-repo-url>
cd insurance_system

Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

**Install dependencies:**

pip install django djangorestframework psycopg2-binary

**Configure the database:**

Ensure MySQL is installed and running.

Update insurance_system/settings.py with your database credentials (e.g., NAME, USER, PASSWORD).

Run migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser (for admin access):

python manage.py createsuperuser

Run the server:

python manage.py runserver

Access the app at http://localhost:8000.

**API Endpoints**
The system provides RESTful APIs for managing resources, secured with token authentication:

Beneficiaries: /api/beneficiaries/ (CRUD operations)
GET: List or filter beneficiaries (e.g., by insurance_id).
POST: Create a new beneficiary.
PUT/PATCH: Update beneficiary details.
DELETE: Remove a beneficiary.
Policies: /api/policies/ (CRUD operations)
GET: List policies or filter by beneficiary.
POST: Create a policy with validation (e.g., end date after start date).
Claims: /api/claims/ (CRUD operations)
GET: List claims or filter by status/priority.
POST: Submit a claim with priority-based processing.
My Contributions
**As the Backend Developer, I focused on building a scalable and secure backend:**

OOP Design: Implemented models (Beneficiary, Policy, Claim) with inheritance, encapsulation (e.g., validators for insurance_id), and polymorphism (e.g., computed age property).
DSA: Optimized performance using:
Hash tables (dictionaries) for O(1) lookups in BeneficiaryViewSet (e.g., filtering by insurance_id).
Priority queues (heapq) in PolicyViewSet and ClaimViewSet for efficient processing based on start date or priority.
Django: Designed modular apps, used Django ORM for efficient queries (e.g., Q objects for search), and implemented class-based views for web interfaces.
DRF: Built RESTful APIs with serializers for validation, pagination for scalability, and token-based authentication for security.
Setup: Configured the project with PostgreSQL, migrations, and admin interfaces for ease of management.
