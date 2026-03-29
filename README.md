# 🚀 FastAPI Items Manager

A production-ready FastAPI application for managing items with Pydantic validation, interactive endpoints, and comprehensive API documentation.

## ✨ Features

- ✅ **Pydantic Models** - Strong data validation with type hints
- ✅ **CRUD Operations** - Create, Read, Update, Delete items
- ✅ **Field Validation** - Constraints on name, description, and price
- ✅ **Interactive API Docs** - Swagger UI and ReDoc
- ✅ **Error Handling** - Proper HTTP status codes and error messages
- ✅ **RESTful Design** - Following REST API best practices
- ✅ **Fast Performance** - Async support with modern Python

## 📋 API Endpoints

### 🏠 Root Endpoint
```
GET /
```
**Response:**
```json
{
  "message": "Welcome to Items Manager API",
  "author": "Rahul"
}
```

### ➕ Create Item
```
POST /items
```
**Request Body:**
```json
{
  "name": "Apple",
  "description": "Fresh red apple",
  "price": 1.99
}
```
**Validation Rules:**
- `name` (required): String, 1-100 characters
- `description` (optional): String, max 500 characters
- `price` (optional): Float, must be ≥ 0

**Example:**
```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Apple",
    "description": "Fresh red apple",
    "price": 1.99
  }'
```

**Response:**
```json
[
  {
    "name": "Apple",
    "description": "Fresh red apple",
    "price": 1.99
  }
]
```

### 📦 Get All Items
```
GET /items?limit=10
```
**Parameters:**
- `limit` (optional): Maximum number of items to return (default: 10)

**Example:**
```bash
curl "http://localhost:8000/items?limit=5"
```

### 📦 Get Item by ID
```
GET /items/{item_id}
```
**Parameters:**
- `item_id` (integer): The index of the item to retrieve

**Example:**
```bash
curl "http://localhost:8000/items/0"
```

**Response:**
```json
{
  "id": 0,
  "item": {
    "name": "Apple",
    "description": "Fresh red apple",
    "price": 1.99
  }
}
```

### ✏️ Update Item
```
PUT /items/{item_id}
```
**Parameters:**
- `item_id` (integer): The index of the item to update

**Request Body:**
```json
{
  "name": "Green Apple",
  "description": "Fresh green apple",
  "price": 2.49
}
```

**Example:**
```bash
curl -X PUT "http://localhost:8000/items/0" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Green Apple",
    "description": "Fresh green apple",
    "price": 2.49
  }'
```

### 🗑️ Delete Item
```
DELETE /items/{item_id}
```
**Parameters:**
- `item_id` (integer): The index of the item to delete

**Example:**
```bash
curl -X DELETE "http://localhost:8000/items/0"
```

**Response:**
```json
{
  "message": "Item deleted",
  "deleted_item": { ... },
  "remaining_items": 0
}
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/rahulsingh731/FAST_API.git
cd FAST_API
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install fastapi uvicorn pydantic
```

## 🚀 Running the Server

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## 📚 Interactive Documentation

Once the server is running, visit:
- **Swagger UI** → `http://localhost:8000/docs` - Interactive testing interface
- **ReDoc** → `http://localhost:8000/redoc` - Beautiful API reference

## 🧪 Testing the API

### Using Swagger UI (Recommended)
1. Go to `http://localhost:8000/docs`
2. Click on each endpoint to expand
3. Click "Try it out" button
4. Enter parameters and click "Execute"

### Using cURL

**Create items:**
```bash
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Apple", "description": "Fresh red apple", "price": 1.99}'

curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Banana", "description": "Yellow banana", "price": 0.99}'
```

**Get all items:**
```bash
curl http://localhost:8000/items
```

**Get item by ID:**
```bash
curl http://localhost:8000/items/0
```

**Update item:**
```bash
curl -X PUT "http://localhost:8000/items/0" \
  -H "Content-Type: application/json" \
  -d '{"name": "Green Apple", "description": "Fresh green apple", "price": 2.49}'
```

**Delete item:**
```bash
curl -X DELETE "http://localhost:8000/items/0"
```

### Using Python requests
```python
import requests

# Create an item
response = requests.post(
    "http://localhost:8000/items",
    json={"name": "Apple", "description": "Fresh red apple", "price": 1.99}
)
print(response.json())

# Get item
response = requests.get("http://localhost:8000/items/0")
print(response.json())
```

### Running Tests
```bash
python test_api.py
```

## 📊 Data Models

### Item Model
| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| name | string | Yes | 1-100 characters |
| description | string | No | Max 500 characters |
| price | float | No | Must be ≥ 0 |

## 🚨 Error Handling

The API returns appropriate HTTP status codes:
- `200 OK` - Successful request
- `404 Not Found` - Item not found
- `422 Unprocessable Entity` - Validation error (invalid data)
- `500 Internal Server Error` - Server error

### Example Error Response
```json
{
  "detail": [
    {
      "type": "value_error.number.not_ge",
      "loc": ["body", "price"],
      "msg": "ensure this value is greater than or equal to 0",
      "input": -5.99
    }
  ]
}
```

## 📄 Project Files

```
FAST_API/
├── main.py                    # FastAPI application with Pydantic models
├── test_api.py               # API test suite
├── README.md                 # This file
├── VALIDATION_REPORT.md      # Comprehensive validation report
└── .venv/                    # Virtual environment
```

## ✨ Key Technologies

- **FastAPI** - Modern async web framework for Python
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - Lightning-fast ASGI web server
- **Python 3.13** - Latest Python version support

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Rahul Singh**

---

**Happy Coding! 🎉**
