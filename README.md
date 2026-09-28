# Task Management API

A structured 3-tier monolithic Task Management API built with Python and Flask.

## Architecture

The application follows a 3-tier architecture:

### Presentation Layer

Located in:

`src/controllers/`

The Controller layer handles HTTP requests and responses. It does not contain business rules or directly access data storage.

### Business Logic Layer

Located in:

`src/services/`

The Service layer contains the application's business rules and validation logic.

### Data Access Layer

Located in:

`src/repositories/`

The Repository layer manages task storage and data access operations.

## Request Flow

```text
HTTP Request

↓

Controller

↓

Service

↓

Repository

↓

Data Storage
```

## Project Structure

```text
task-api/
├── src/
│   ├── controllers/
│   │   └── task_controller.py
│   ├── repositories/
│   │   └── task_repository.py
│   └── services/
│       └── task_service.py
├── app.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Requirements

* Python 3.10+
* Flask

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd task-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command:

```bash
python app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint      | Description   |
| ------ | ------------- | ------------- |
| GET    | `/tasks`      | Get all tasks |
| GET    | `/tasks/<id>` | Get a task    |
| POST   | `/tasks`      | Create a task |
| PUT    | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

## Layer Separation

The application maintains strict separation between layers.

### Controllers

Controllers are responsible only for HTTP communication.

### Services

Services contain business rules and validation.

### Repositories

Repositories handle data storage.

This separation improves maintainability and makes individual layers easier to change or test.

## Example Request

### POST `/tasks`

```json
{
    "title": "Learn Software Architecture",
    "description": "Study 3-tier architecture",
    "status": "pending"
}
```

## Future Improvements

The current implementation uses in-memory storage for simplicity.

Future versions could introduce:

* PostgreSQL or MySQL
* Unit tests
* Authentication
* Error-handling middleware
* Logging
* Docker
* API documentation
