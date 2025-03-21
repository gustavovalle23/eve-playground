# **Eve Playground**

A simple backend application using **Eve**, **Pydantic**, and **MongoDB** in a **Docker** container. The project is designed to demonstrate a scalable and modular structure for building APIs with **Eve** while utilizing **Pydantic** for data validation and environment variables for configuration.

---

## **Table of Contents**
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Setup](#setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Install Dependencies](#2-install-dependencies)
  - [3. Run MongoDB in Docker](#3-run-mongodb-in-docker)
  - [4. Set Up Environment Variables](#4-set-up-environment-variables)
  - [5. Run the Application](#5-run-the-application)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

---

## **Project Overview**

This project is a simple demonstration of building a scalable REST API backend using **Eve**, a REST API framework built on top of **Flask**. The app utilizes **Pydantic** for input validation, **MongoDB** for data storage (hosted inside a **Docker** container), and environment variables loaded via **`.env`** for configuration.

The goal is to show how to structure an **Eve** API application in a modular way, including good practices for project organization, data validation, and use of environment variables for configurations.

---

## **Tech Stack**

- **Eve**: REST API framework built on Flask.
- **Pydantic**: Data validation and settings management.
- **MongoDB**: Database for storing user data.
- **Docker**: Used for running MongoDB in a containerized environment.
- **Python**: The main programming language used.
- **Flask**: Web framework used by Eve.
- **Python-dotenv**: For managing environment variables via `.env` file.

---

## **Requirements**

- **Python** 3.9 or higher
- **Docker** (for MongoDB container)
- **pip** (Python package installer)

---

## **Setup**

### **1. Clone the Repository**

Clone the repository to your local machine:
```bash
git clone https://github.com/gustavovalle23/eve-playground.git
cd eve-playground
```

### **2. Install Dependencies**

Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### **3. Run MongoDB in Docker**

Ensure **Docker** is installed and running on your machine. Then, use Docker to run MongoDB:

```bash
docker-compose up -d
```

This will pull the official MongoDB image and run it in a container.

### **4. Set Up Environment Variables**

Create a `.env` file in the project root and define the following variables:

```ini
MONGO_URI=mongodb://localhost:27017
MONGO_DBNAME=mydatabase
DEBUG=True
```

This ensures that your app is connected to the local MongoDB instance and the app runs in debug mode.

### **5. Run the Application**

Now you can run the application using:

```bash
python -m app.main
```

This will start the Eve API on `http://127.0.0.1:5000`.

---

## **Usage**

Once the application is running, you can interact with the API via HTTP requests.

### **Create a User**
```bash
curl -X POST "http://127.0.0.1:5000/users" \
-H "Content-Type: application/json" \
-d '{"username": "john_doe", "email": "john@example.com", "age": 30}'
```

### **Get All Users**
```bash
curl -X GET "http://127.0.0.1:5000/users"
```

---

## **API Endpoints**

- `POST /users` - Create a new user.
- `GET /users` - Retrieve all users.
- `GET /users/<user_id>` - Retrieve a single user by ID.
- `PATCH /users/<user_id>` - Update a user.
- `DELETE /users/<user_id>` - Delete a user.

---

## **Project Structure**

The folder structure of the project is designed to be scalable and modular:

```
backend/
│── app/
│   ├── models/            # Database models
│   │   ├── user.py
│   │   ├── __init__.py
│   ├── schemas/           # Pydantic schemas for validation
│   │   ├── user.py
│   │   ├── __init__.py
│   ├── settings.py        # Eve settings and MongoDB configuration
│   ├── main.py            # Eve app instance
│   ├── __init__.py
│── .env                   # Environment variables
│── docker-compose.yml      # MongoDB in Docker
│── requirements.txt        # Project dependencies
│── README.md               # Documentation
```


---

## **Contributing**

Contributions are welcome! Feel free to open an issue or submit a pull request. If you want to improve the project or have ideas for new features, let me know.

Steps to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to your branch (`git push origin feature-name`)
5. Create a new Pull Request
