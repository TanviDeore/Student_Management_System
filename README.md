# Student Management System

A simple student management system built using Python's Tkinter library for the graphical user interface (GUI). The application allows the user to add, view, update, delete, and visualize student records stored in an Oracle database. The system also features a temperature display, quote of the day, and a bar graph of student marks.

## Features

- **Add Student**: Allows the user to input student roll number, name, and marks.
- **View Students**: Displays a list of all student records.
- **Update Student**: Allows the user to modify existing student details.
- **Delete Student**: Deletes a student record based on the roll number.
- **Bar Graph**: Visualizes the performance of all students as a bar chart.
- **Quote of the Day**: Fetches and displays a quote from the BrainyQuote API.
- **Weather Temperature**: Displays the current temperature of a given city (e.g., Mumbai) using the OpenWeather API.

## Prerequisites

- Python 3.x
- Tkinter library (comes pre-installed with Python)
- `cx_Oracle` library (for Oracle database connectivity)
- `requests` library (for fetching weather and quote data)
- `matplotlib` library (for generating bar graphs)
- `playsound` library (for playing sound on record insertion)
- Oracle database setup with a `student` table for storing student records.

## Installation

1. Install the required libraries:

   ```bash
   pip install cx_Oracle requests matplotlib playsound

2. Set up an Oracle database with a table to store student data. The student table should have the following schema:
   CREATE TABLE student (
  rno INT PRIMARY KEY,
  name VARCHAR2(100),
  marks INT
  );

3. Update the Oracle database connection credentials in the code. The connection string in the code is:
   con = cx_Oracle.connect('system/abc123')  # Modify with your database credentials

## How to Use

1. Run the Python script:

   python student_management_system.py

The main GUI window will open with the following options:

   Add: Add a new student record.
   View: View all student records.
   Update: Update an existing student record.
   Delete: Delete a student record.
   Graph: View a bar graph of student marks.

The application also displays the quote of the day and the current temperature of Mumbai.
