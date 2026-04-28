# API Testing Framework (Pytest)

## Overview

This project is a basic API testing framework built using Python.
It uses pytest to validate REST API endpoints.

---

## Tech Stack

* Python
* pytest
* requests

---

## Project Structure

```
api-test-framework/
│── tests/
│   ├── test_users.py
│   ├── test_posts.py
│
│── utils/
│   ├── api_client.py
│
│── requirements.txt
```

---

## Setup

### 1. Create virtual environment

```
python -m venv venv
venv\Scripts\Activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## Run Tests

```
pytest -v
```

---

## Sample Tests

* Check API status codes
* Validate response structure
* Test invalid endpoints

---

## Author

https://github.com/Amulyagollum
