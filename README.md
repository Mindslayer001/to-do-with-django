# Todo App with Django

## Pre-Requisites:
To complete this project, you must be required to download the following:
- **Any IDE:** Install any IDE like Visual Studio Code. [Download VS Code from Here](https://code.visualstudio.com/)
- **Python:** A solid understanding of Python programming language syntax, data structures, and control flow is crucial.
- **Web Development Fundamentals:** Familiarity with basic web development concepts like HTTP requests and responses, HTML templating, and working with a web server (like Apache or Nginx) will be beneficial.
- **Package Manager:** Poetry is a dependency management tool for Python projects. 
- **Virtual Environment:** It's recommended to use a virtual environment to isolate project dependencies. Create a virtual environment using the following command:
```bash
  poetry new to-do
  poetry shell
  ```
- **Django Framework:** This is the core framework used to build the web application. To install Django you can use the following command:
  ```bash
  poetry add django
  ```

## Project Setup:
1. To create a new Django project, navigate to your desired project directory and run the following command to create a new project:
   ```bash
   django-admin startproject config .
   ```
2. Navigate to the root directory of your Django project and then run the following command to create a new Django application:
   ```bash
   python manage.py startapp toDo
   ```

## Objective:
The objective of this project is to develop a user-friendly web application for managing todo tasks. Ronaldo seeks a tool that simplifies task management with features to add, view, edit, and delete tasks effortlessly.

## Tasks:
1. **User Interaction:** Users interact with the app through a web interface to perform CRUD (Create, Read, Update, Delete) operations on tasks.
2. **Data Management:** The app stores task data in a database and provides functionality to manipulate this data.
3. **Data Processing:** The app processes user input to perform CRUD operations and updates the database accordingly.
4. **Display Tasks:** The app presents tasks to users in a clear and organized manner, facilitating easy task management.

## Solution Development Procedure:
1. **Views File (`views.py`):** Develop views to handle user requests, interact with task data, and render HTML templates.
   - **CRUD Operations:** Implement functions for adding, viewing, editing, and deleting tasks.
   
2. **URLs File (`urls.py`):** Define URL routes to map user requests to appropriate views.
   - **Path:** Define URL patterns for different CRUD operations.
   - **View Function:** Associate view functions with URL patterns to handle user requests.
   - **Name:** Assign names to URL patterns for easy reference in the Django application.
   
3. **Models (`models.py`):** Define models to represent todo tasks in the database.
   - **TodoItem Model:** Define fields such as title, description, completed, and created_at to represent todo tasks.
   - **Relationships:** Establish relationships between todo items and users if required (e.g., one-to-many relationship).
   
4. **Forms (`forms.py`):** Create forms to handle user input for adding and editing tasks.
   - **TodoForm:** Define form fields corresponding to todo item attributes (e.g., title and description).
   - **Validation:** Implement validation rules to ensure data integrity and prevent errors.
## Preview 
[!preview](assests/Screenshot%20from%202024-05-13%2016-45-16.png)
