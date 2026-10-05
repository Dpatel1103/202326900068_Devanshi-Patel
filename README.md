# Student CRUD API

A simple REST API for creating, viewing, updating, and deleting student records. The API is built with FastAPI and validates request data with Pydantic.

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project structure

```text
student-crud/
├── main.py
├── models/
│   └── student_model.py
├── routes/
│   └── student_routes.py
├── controllers/
│   └── student_controller.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Student fields

| Field | Type | Validation |
| --- | --- | --- |
| `id` | Integer | Required |
| `name` | String | Required |
| `email` | String | Required; must be a valid email address |
| `course` | String | Required |
| `semester` | Integer | Required |

Pydantic returns **422 Unprocessable Entity** when request data fails validation.

## API endpoints

| Method | Endpoint | Description | Status codes |
| --- | --- | --- | --- |
| `POST` | `/students` | Create a student | `201 Created`, `409 Conflict` if the ID already exists, `422` for invalid data |
| `GET` | `/students` | List all students | `200 OK` |
| `GET` | `/students/{id}` | Get a student by ID | `200 OK`, `404 Not Found` |
| `PUT` | `/students/{id}` | Update a student by ID | `200 OK`, `404 Not Found`, `422` for invalid data |
| `DELETE` | `/students/{id}` | Delete a student by ID | `204 No Content`, `404 Not Found` |

## Example student JSON

```json
{
  "id": 1,
  "name": "Asha Patel",
  "email": "asha@example.com",
  "course": "Computer Science",
  "semester": 3
}
```

## Installation

Run these commands from the project directory:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the application

From the project directory, start the development server:

```bash
uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive Swagger documentation is at <http://127.0.0.1:8000/docs>.

## Storage

Student records are kept only in a local in-memory Python dictionary. **This project does not use a database.** Records are lost when the application stops.
