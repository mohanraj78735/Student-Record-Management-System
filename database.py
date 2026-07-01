import sqlite3
import pandas as pd

DATABASE = "students.db"


# Database Connection
def get_connection():
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    return conn


# Create Table
def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT UNIQUE NOT NULL,
            department TEXT,
            year TEXT,
            email TEXT,
            phone TEXT
        )
    """)

    conn.commit()
    conn.close()


# Add Student
def add_student(name, roll_no, department, year, email, phone):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students(name, roll_no, department, year, email, phone)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, roll_no, department, year, email, phone))

    conn.commit()
    conn.close()


# View All Students
def get_students():
    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM students ORDER BY id DESC",
        conn
    )

    conn.close()
    return df


# Search Student
def search_student(roll_no):
    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM students WHERE roll_no=?",
        conn,
        params=(roll_no,)
    )

    conn.close()
    return df


# Update Student
def update_student(name, department, year, email, phone, roll_no):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE students
        SET
            name=?,
            department=?,
            year=?,
            email=?,
            phone=?
        WHERE roll_no=?
    """, (name, department, year, email, phone, roll_no))

    conn.commit()
    conn.close()


# Delete Student
def delete_student(roll_no):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll_no,)
    )

    conn.commit()
    conn.close()


# Dashboard Count
def total_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")

    total = cursor.fetchone()[0]

    conn.close()

    return total


# Export CSV
def export_csv():
    df = get_students()
    df.to_csv("students.csv", index=False)


# Export Excel
def export_excel():
    df = get_students()
    df.to_excel("students.xlsx", index=False)
