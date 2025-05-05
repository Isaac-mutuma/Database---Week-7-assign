# 📦 Database Management System + CRUD API Project

## Overview

This project is divided into two main parts:

### 🔹 Question 1: MySQL Relational Database Design  
**Objective:** Build a complete, well-structured relational database for a real-world use case using only SQL.

### 🔹 Question 2: CRUD API with MySQL + FastAPI  
**Objective:** Use FastAPI (Python) to create a fully functional CRUD API connected to the MySQL database.

---

## Question 1: MySQL Relational Database

### 🏥 Use Case: Photography Client Management System

This database is designed to manage photography studio operations, including clients, photo sessions, packages, and payments.

### 📁 Files

- `photography_db.sql`: Contains all SQL `CREATE TABLE` statements and sample `INSERT` data.

### 🗃️ Tables and Structure

1. **clients**
   - `client_id` (Primary Key, Auto Increment)
   - `full_name` (VARCHAR, NOT NULL)
   - `email` (VARCHAR, UNIQUE, NOT NULL)
   - `phone_number` (VARCHAR, NOT NULL)

2. **photo_sessions**
   - `session_id` (Primary Key, Auto Increment)
   - `client_id` (Foreign Key → clients)
   - `session_date` (DATE)
   - `location` (VARCHAR)
   - `status` (ENUM: 'Pending', 'Completed', 'Cancelled')

3. **packages**
   - `package_id` (Primary Key, Auto Increment)
   - `package_name` (VARCHAR, NOT NULL)
   - `description` (TEXT)
   - `price` (FLOAT)

4. **payments**
   - `payment_id` (Primary Key, Auto Increment)
   - `session_id` (Foreign Key → photo_sessions)
   - `amount_paid` (FLOAT)
   - `payment_method` (VARCHAR)

### 🔗 Relationships

- One client can have multiple sessions (1:M)
- Each session can have multiple payments (1:M)

---

## 📘 Question 2: CRUD API with FastAPI + MySQL

### 🔧 Technologies Used

- **Python 3**
- **FastAPI**
- **MySQL**
- **Pydantic**
- **Uvicorn**

### 📁 Main File

- `main.py`: Contains all FastAPI routes for clients, sessions, packages, and payments.

### 📌 API Endpoints

#### 🔹 Clients
- `POST /clients` – Add new client
- `GET /clients` – List all clients
- `PUT /clients/{client_id}` – Update client info
- `DELETE /clients/{client_id}` – Remove client

#### 🔹 Sessions
- `POST /sessions` – Schedule a new session
- `GET /sessions` – Get all sessions
- `PUT /sessions/{session_id}` – Update session details
- `DELETE /sessions/{session_id}` – Cancel session

#### 🔹 Packages
- `POST /packages` – Add a new package
- `GET /packages` – List all packages

#### 🔹 Payments
- `POST /payments` – Record a payment
- `GET /payments` – List all payments

###  How to Run the Project

1. **Install dependencies**  
   ```bash
   pip install fastapi uvicorn mysql-connector-python
2. Start the server
   uvicorn main:app --reload
3.Test with Swagger UI
  Open http://127.0.0.1:8000/docs in your browser.
