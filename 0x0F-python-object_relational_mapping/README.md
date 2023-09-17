# 0x0F - Python Object-Relational Mapping

## Project Overview

This is a Python project that explores the world of Object-Relational Mapping (ORM) by connecting Python with MySQL databases. This project is designed to help you understand how to use Python to interact with databases and perform various database operations without writing raw SQL queries. It also introduces you to the SQLAlchemy library, which is a powerful ORM tool.

## Project Tasks

The project consists of several tasks, each of which focuses on different aspects of Python, MySQL, and SQLAlchemy. Here's a brief overview of the tasks to be working on:

### Task 0: Get all states

- Write a Python script to list all states from the "hbtn_0e_0_usa" database.
- Use the MySQLdb module to connect to the MySQL database.
- Sort the results by state ID in ascending order.

### Task 1: Filter states

- Write a Python script to list states with names starting with the letter "N" (uppercase).
- Connect to the "hbtn_0e_0_usa" database using MySQLdb.
- Sort the results by state ID in ascending order.

### Task 2: Filter states by user input

- Create a Python script that takes a state name as input and lists matching states from the database.
- Connect to the "hbtn_0e_0_usa" database using MySQLdb.
- Use user input to filter states.
- Sort the results by state ID in ascending order.

### Task 3: SQL Injection...

- Write a Python script to list states while protecting against SQL injection.
- Connect to the "hbtn_0e_0_usa" database using MySQLdb.
- Implement measures to prevent SQL injection.

### Task 4: Cities by states

- Create a Python script to list all cities from the "hbtn_0e_4_usa" database.
- Connect to the MySQL database using MySQLdb.
- Sort the results by city ID in ascending order.

### Task 5: All cities by state

- Write a Python script that lists all cities in a specified state from the "hbtn_0e_4_usa" database.
- Connect to the MySQL database using MySQLdb.
- Sort the results by city ID in ascending order.

### Task 6: First state model

- Define a Python class for the "State" table using SQLAlchemy.
- Create a declarative base instance.
- This task sets up the foundation for using SQLAlchemy ORM.

### Task 7: All states via SQLAlchemy

- Write a Python script to list all state objects from the "hbtn_0e_6_usa" database using SQLAlchemy.
- Connect to the MySQL database using SQLAlchemy.
- Sort the results by state ID in ascending order.

### Task 8: First state

- Create a Python script to retrieve and display the first state from the "hbtn_0e_6_usa" database using SQLAlchemy.
- Connect to the MySQL database using SQLAlchemy.
- Display the state with the lowest state ID.

### Task 9: Contains 'a'

- Write a Python script to list states that contain the letter 'a' from the "hbtn_0e_6_usa" database using SQLAlchemy.
- Connect to the MySQL database using SQLAlchemy.
- Sort the results by state ID in ascending order.

### Task 10: Get a state

- Create a Python script to retrieve a state by name from the "hbtn_0e_6_usa" database using SQLAlchemy.
- Connect to the MySQL database using SQLAlchemy.
- Display the state's ID or "Not found" if the state doesn't exist.

### Task 11: Add a new state

- Write a Python script to add a new state, "Louisiana," to the "hbtn_0e_6_usa" database using SQLAlchemy.
- Connect to the MySQL database using SQLAlchemy.
- Display the new state's ID after creation.

### Task 12: Update a state

- Create a Python script to change the name of a state in the "hbtn_0e_6_usa" database using SQLAlchemy.
- Connect to the MySQL database using SQLAlchemy.
- Change the name of the state with ID 2 to "New Mexico."

### Task 13: Delete states

- Write a Python script to delete states with names containing the letter 'a' from the "hbtn_0e_6_usa" database using SQLAlchemy.
- Connect to the MySQL database using SQLAlchemy.

### Task 14: Cities in state

- Define a Python class for the "City" table using SQLAlchemy.
- Create a script to list all City objects from the "hbtn_0e_14_usa" database.
- Connect to the MySQL database using SQLAlchemy.
- Sort the results by city ID in ascending order.
- Display results in the format "<state name>: (<city id>) <city name>."

## Getting Started

Before you begin, make sure you have the following prerequisites:

- MySQL server installed and running (MySQL 8.0 recommended).
- Python 3

.x installed on your system.
- Required Python packages installed, such as MySQLdb, SQLAlchemy, etc.

To get started with this project, follow these steps:

1. Clone the Arepo repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/arepo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd arepo
   ```

3. Install the required Python packages if you haven't already:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a MySQL database named "hbtn_0e_0_usa" for Task 0 and "hbtn_0e_6_usa" for Tasks 6-13, and "hbtn_0e_4_usa" for Tasks 4-5. Import the provided SQL dump files if available.

5. Review the tasks and corresponding Python scripts in the project directory.

6. Run each script as needed for the specific task you want to complete.

7. Enjoy exploring Object-Relational Mapping (ORM) with Python and MySQL!

## Project Structure

Here's a brief overview of the project structure:

- **scripts**: Contains Python scripts for each task.
- **sql**: Contains SQL dump files for database setup (if available).
- **models**: Contains SQLAlchemy model definitions for the "State" and "City" tables.
- **tests**: Place your test scripts here (optional).
- **requirements.txt**: Lists the required Python packages for this project.
