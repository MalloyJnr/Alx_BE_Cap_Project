# Church Contribution Management System (Backend API)

## Project Overview
This is a backend REST API built with Django and Django REST Framework for managing church members and their financial contributions, including dues, welfare, and offerings.

The system allows authenticated users to:
- Manage church members
- Record different types of contributions
- View contribution summaries per member

## Features
- Token-based authentication
- Member management (CRUD)
- Contribution tracking (Dues, Welfare, Offering)
- Automatic contribution summaries per member
- Secure, authenticated API endpoints

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (development)

## API Endpoints (Sample)
- POST `/api/auth/login/`
- GET / POST `/api/members/`
- GET / POST `/api/contributions/`

## Authentication
This API uses token-based authentication.
Include the token in request headers:


## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
4. Run migrations:
5. Start the server:

## Project Status
This project is currently in development as part of a capstone project.
Additional features such as reporting, permissions, and testing will be
implemented in future phases.
