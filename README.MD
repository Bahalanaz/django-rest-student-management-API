🐍 Django REST Student Management API

This repository documents my progress in building a Django-based backend system focused on REST-style API development, database design using ORM, and authentication handling.

The project represents a transition from Python logic-based programming into structured backend engineering using Django.

🚀 Project Overview

This Django backend system allows me to:

Build a Django project and app structure from scratch
Design database models using Django ORM
Perform full CRUD operations (Create, Read, Update, Delete)
Implement REST-style API endpoints using Django views
Handle JSON-based request and response systems
Work with dynamic URL routing and resource-based endpoints
Implement session-based authentication (login/logout)
Understand request → response lifecycle in Django
Apply backend separation of concerns (models, views, URLs)

This project simulates a real-world backend API system without using Django REST Framework, to deeply understand how Django works internally.

🧠 Concepts Learned
1. Django Project Architecture

A Django project is structured into:

Core project configuration
Application modules
URL routing system
Settings and environment configuration

👉 Core Idea: Django follows a modular architecture to separate responsibilities into reusable apps.

2. Django Apps (Modular Design)

Each app represents a backend feature:

Student_Management → main API system
Future apps can include authentication, payments, etc.

👉 Core Idea: Each app acts like a microservice inside a monolithic framework.

3. Models (Database Layer)

Models define database structure using Python classes.

👉 Core Idea: Django ORM automatically converts Python classes into database tables.

4. Django ORM

Used for database operations without SQL:

Create records
Read records
Update records
Delete records

👉 Core Idea: ORM abstracts SQL into Python-based queries.

5. Migrations

Migrations handle database schema changes:

Model changes → migration file → database update

👉 Core Idea: Migrations act as version control for databases.

6. URL Routing System

URLs map requests to backend logic:

Static routes
Dynamic routes (with parameters like ID)

👉 Core Idea: URLs represent resources, not functions.

7. Views (Backend Logic Layer)

Views handle:

Request processing
Business logic
Response generation

👉 Core Idea: Views act as controllers in backend architecture.

8. JSON API Responses

All responses are returned in JSON format:

Structured data exchange
Frontend-backend communication standard

👉 Core Idea: Modern APIs communicate using JSON.

9. Authentication System (Session-Based)

Implemented login/logout using Django authentication:

authenticate()
login()
logout()

👉 Core Idea: Backend systems must secure access using authentication layers.

10. CRUD Operations (Core Backend Logic)

Implemented full CRUD system:

Create student
Retrieve students
Update student
Delete student

👉 Core Idea: All backend systems revolve around CRUD operations on resources.

11. Request → Response Lifecycle

Django processes requests in this flow:

Client → URL → View → ORM → Response

👉 Core Idea: This is the foundation of all backend APIs.

🛠️ Features

🗂️ Database System
Student model with name, age, course fields
SQLite database powered by Django ORM

🔐 Authentication System
User login and logout system
Session-based authentication handling
Protected API endpoints

🌐 REST-Style API System
JSON-based API responses
CRUD endpoints for student management
Resource-based URL design

🔗 URL System
Clean REST-style routing
Dynamic endpoints using IDs
Separation of API logic per endpoint

🧪 Backend Development Skills Practiced
Django project setup from scratch
App-based modular architecture
ORM-based database design
REST-style API creation
Authentication handling
JSON API response formatting
Git version control workflow
Backend debugging and error handling

🧠 Key Takeaways
Django is a full backend framework, not just a library
ORM replaces manual SQL queries
APIs should return structured JSON data
Authentication is essential for backend security
URLs should represent resources, not actions
Backend systems are layered and modular
Proper project structure is critical for scalability

🚀 Outcome

By completing this project, I now understand:

How Django processes requests internally
How models map to database tables
How REST-style APIs are built using Django
How authentication works in backend systems
How real backend architecture is structured

This project forms a strong foundation for:

Django REST Framework
JWT authentication systems
Production-level backend APIs
Scalable backend architecture designs