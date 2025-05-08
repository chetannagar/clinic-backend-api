# Clinic Web App API - Streamlining Healthcare Operations

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yourusername/clinic-web-app/pulls)

This project is a comprehensive web application designed to streamline clinic operations, enhance patient experiences, and modernize healthcare management. It provides features like appointment scheduling, patient record management, and communication tools, all through a user-friendly digital platform.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Getting Started](#getting-started)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The Clinic Web App addresses common challenges faced by clinics, such as inefficient appointment scheduling, manual record-keeping, and communication gaps. By implementing features like self-service appointment booking, digital patient profiles, and automated reminders, the platform improves operational efficiency and patient satisfaction.

---

## Features

### Core Features

- **Online Appointment Booking:** Patients can schedule, reschedule, and cancel appointments online.
- **Automated Notifications:** Email and SMS reminders to reduce no-shows.
- **Digital Patient Records:** Secure storage of consultation history, prescriptions, and medical reports.
- **Doctor Dashboard:** Centralized management of appointments and patient records.
- **Admin Panel:** Comprehensive system management and user access control.
- **Real-time Availability:** Prevents double bookings and scheduling conflicts.

### Planned Features

- **Tele-consultation Support:** Integration for virtual doctor consultations.
- **Online Payments:** Integration with payment gateways for seamless transactions.

---

## Architecture

The application follows a modular architecture:

### Frontend

- **Patient Portal:** Built with React/Next.js for patient-facing functionalities.
- **Doctor/Admin Portal:** Built with React/Next.js for clinic staff and administrators.

### Backend

- **RESTful API:** Built with Django, handling business logic and data management.

### Database

- **PostgreSQL:** Relational database for structured data.

### Third-Party Services

- **Firebase Auth:** For secure authentication.
- **Twilio/SendGrid:** For SMS and email notifications.
- **AWS S3:** For file storage.

---

## Tech Stack

- **Backend:** Django 5.2, Django REST Framework
- **Database:** PostgreSQL
- **Frontend:** React/Next.js (planned)
- **Authentication:** Firebase Auth
- **Notifications:** Twilio (SMS), SendGrid (Email)
- **File Storage:** AWS S3
- **Testing:** Django TestCase, Factory Boy, Faker
- **Deployment:** Docker (planned)

---

## Database Schema

The database schema includes the following key models:

### Users

- **User:** Handles authentication and user roles (Patient, Doctor, Admin, Staff).

### Patients

- **Patient:** Stores patient-specific details like date of birth, gender, address, and emergency contact.

### Doctors

- **Doctor:** Stores doctor-specific details like specialization, qualifications, and experience.
- **DoctorAvailability:** Tracks doctor availability by day and time.

### Appointments

- **Appointment:** Manages appointment scheduling, status, and associated details.

### Reports

- **MedicalReport:** Stores medical reports linked to patients and their appointments.
- **Prescription:** Stores prescriptions with medications and instructions.

### Payments

- **Payment:** Tracks payment details, including method and transaction status.
- **Invoice:** Stores invoice details for appointments.

### Notifications

- **Notification:** Manages SMS and email notifications for users.
- **Message:** Tracks messages between users.

### Clinic Settings

- **ClinicSetting:** Stores key-value pairs for clinic configurations.
- **Review:** Tracks patient reviews for doctors.
- **AuditLog:** Logs user actions for auditing purposes.
- **AdminActionLog:** Logs admin-specific actions.

---

## API Endpoints

### 1️⃣ **Authentication & User Management**

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| POST | /api/auth/register/ | Register a new user (Patient) | ❌ |
| POST | /api/auth/register/doctor/ | Register a new doctor (Requires approval) | ❌ |
| POST | /api/auth/login/ | Login using Firebase | ❌ |
| GET | /api/users/me/ | Get current user details | ✅ |
| PUT | /api/users/update/ | Update user profile | ✅ |
| DELETE | /api/users/delete/ | Delete user account | ✅ (Admin) |
| GET | /api/doctors/list/ | List all doctors | ✅ |
| GET | /api/doctors/{id}/ | Get doctor details | ✅ |
| PUT | /api/doctors/{id}/approve/ | Approve a doctor account | ✅ (Admin) |

### 2️⃣ **Appointments (Patient-Doctor Booking System)**

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| GET | /api/doctors/{id}/availability/ | Check doctor availability | ✅ |
| POST | /api/appointments/book/ | Book a new appointment | ✅ |
| GET | /api/appointments/list/ | List all appointments (for a user) | ✅ |
| GET | /api/appointments/{id}/ | Get details of an appointment | ✅ |
| PUT | /api/appointments/{id}/update/ | Reschedule or modify an appointment | ✅ |
| PUT | /api/appointments/{id}/status/ | Update appointment status (Completed, No-show) | ✅ (Doctor) |
| DELETE | /api/appointments/{id}/cancel/ | Cancel an appointment | ✅ |

### 3️⃣ **Medical Reports (Doctors Uploading Patient Reports)**

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| POST | /api/reports/upload/ | Upload a medical report (PDF, Image) | ✅ (Doctor) |
| GET | /api/reports/{id}/ | View a medical report | ✅ |
| GET | /api/reports/patient/{patient_id}/ | View all reports for a patient | ✅ (Doctor) |
| DELETE | /api/reports/{id}/delete/ | Delete a report | ✅ (Doctor) |
| POST | /api/prescriptions/create/ | Create a new prescription | ✅ (Doctor) |
| GET | /api/prescriptions/{id}/ | Get prescription details | ✅ |
| GET | /api/prescriptions/patient/{patient_id}/ | Get prescriptions for a patient | ✅ (Doctor) |
| PUT | /api/prescriptions/{id}/update/ | Update a prescription | ✅ (Doctor) |
| DELETE | /api/prescriptions/{id}/delete/ | Delete a prescription | ✅ (Doctor) |

### 4️⃣ **Notifications (Reminders via SMS & Email)**

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| POST | /api/notifications/send/ | Send notification (Twilio/SendGrid) | ✅ (Admin) |
| GET | /api/notifications/list/ | List all notifications sent | ✅ |
| GET | /api/notifications/{id}/ | Get details of a notification | ✅ |
| PUT | /api/notifications/{id}/read/ | Mark notification as read | ✅ |

### 5️⃣ **Payments (Optional – If Monetization is Added)**

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| POST | /api/payments/charge/ | Make a payment for an appointment | ✅ |
| GET | /api/payments/history/ | Get payment history for a user | ✅ |
| GET | /api/payments/{id}/ | Get details of a transaction | ✅ |
| POST | /api/invoices/generate/ | Generate an invoice for a completed appointment | ✅ |
| GET | /api/invoices/{id}/ | Get invoice details | ✅ |

### 6️⃣ **Admin & Audit Logs**

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| GET | /api/audit-logs/list/ | Get all audit logs | ✅ (Admin) |
| GET | /api/audit-logs/{id}/ | Get details of a specific log | ✅ (Admin) |

---

## Getting Started

### Prerequisites

- Python 3.13
- PostgreSQL
- Node.js (for frontend development)
- Docker (optional, for deployment)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/clinic-web-app.git
    cd clinic-web-app/clinic_backend_api
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Populate the database with dummy data:

    ```bash
    python manage.py populate_db_master
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

---

## Development

### Testing

Run tests using Django's test framework:

```bash
python [manage.py](http://_vscodecontentref_/1) test
