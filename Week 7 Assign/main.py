from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="MySql",           # ✅ Use your actual MySQL username
        password="395400My",   # ✅ Use your actual MySQL password
        database="photographydb"  # ✅ Use your correct DB name
    )

    

# Models
class Client(BaseModel):
    full_name: str
    email: str
    phone_number: str

class Session(BaseModel):
    client_id: int
    session_date: str
    location: str
    status: str  # 'Pending', 'Completed', 'Cancelled'

class Package(BaseModel):
    package_name: str
    description: str
    price: float

class Payment(BaseModel):
    session_id: int
    amount_paid: float
    payment_method: str

# Clients CRUD
@app.post("/clients")
def create_client(client: Client):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clients (full_name, email, phone_number)
        VALUES (%s, %s, %s)
    """, (client.full_name, client.email, client.phone_number))
    conn.commit()
    return {"message": "Client added successfully"}

@app.get("/clients")
def get_clients():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clients")
    return cursor.fetchall()

@app.put("/clients/{client_id}")
def update_client(client_id: int, client: Client):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clients SET full_name=%s, email=%s, phone_number=%s
        WHERE client_id=%s
    """, (client.full_name, client.email, client.phone_number, client_id))
    conn.commit()
    return {"message": "Client updated successfully"}

@app.delete("/clients/{client_id}")
def delete_client(client_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE client_id=%s", (client_id,))
    conn.commit()
    return {"message": "Client deleted successfully"}

# Sessions CRUD
@app.post("/sessions")
def create_session(session: Session):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO photo_sessions (client_id, session_date, location, status)
        VALUES (%s, %s, %s, %s)
    """, (session.client_id, session.session_date, session.location, session.status))
    conn.commit()
    return {"message": "Session added successfully"}

@app.get("/sessions")
def get_sessions():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM photo_sessions")
    return cursor.fetchall()

@app.put("/sessions/{session_id}")
def update_session(session_id: int, session: Session):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE photo_sessions SET client_id=%s, session_date=%s, location=%s, status=%s
        WHERE session_id=%s
    """, (session.client_id, session.session_date, session.location, session.status, session_id))
    conn.commit()
    return {"message": "Session updated successfully"}

@app.delete("/sessions/{session_id}")
def delete_session(session_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM photo_sessions WHERE session_id=%s", (session_id,))
    conn.commit()
    return {"message": "Session deleted successfully"}

# Packages CRUD
@app.post("/packages")
def create_package(package: Package):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO packages (package_name, description, price)
        VALUES (%s, %s, %s)
    """, (package.package_name, package.description, package.price))
    conn.commit()
    return {"message": "Package added successfully"}

@app.get("/packages")
def get_packages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM packages")
    return cursor.fetchall()

# Payments CRUD
@app.post("/payments")
def create_payment(payment: Payment):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO payments (session_id, amount_paid, payment_method)
        VALUES (%s, %s, %s)
    """, (payment.session_id, payment.amount_paid, payment.payment_method))
    conn.commit()
    return {"message": "Payment recorded successfully"}

@app.get("/payments")
def get_payments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payments")
    return cursor.fetchall()
