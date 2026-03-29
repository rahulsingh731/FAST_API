# 🚀 FastAPI Items Manager

A simple yet powerful FastAPI application for managing items with interactive endpoints.

## ✨ Features

- ✅ Create and manage items
- ✅ Retrieve items by ID
- ✅ Interactive API documentation
- ✅ Fast and modern Python web framework

## 📋 Endpoints

### 🏠 Root Endpoint
```
GET /
```
**Response:**
```json
{
  "Hello": "Rahul"
}
```

### ➕ Create Item
```
POST /items?item={item_name}
```
**Parameters:**
- `item` (string): The name of the item to add

**Example:**
```bash
curl -X POST "http://localhost:8000/items?item=apple"
```

**Response:**
```json
["apple"]
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
"apple"
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
pip install fastapi uvicorn
```

## 🚀 Running the Server

```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## 📚 Interactive Documentation

Once the server is running, visit:
- **Swagger UI** → `http://localhost:8000/docs`
- **ReDoc** → `http://localhost:8000/redoc`

## 🧪 Test the API

### Try in Swagger UI
1. Go to `http://localhost:8000/docs`
2. Click on each endpoint to expand
3. Click "Try it out" button
4. Enter parameters and click "Execute"

### Try with cURL

```bash
# Get root
curl http://localhost:8000/

# Add items
curl -X POST "http://localhost:8000/items?item=apple"
curl -X POST "http://localhost:8000/items?item=banana"
curl -X POST "http://localhost:8000/items?item=orange"

# Get items by index
curl http://localhost:8000/items/0
curl http://localhost:8000/items/1
curl http://localhost:8000/items/2

# Get non-existent item (404 error)
curl http://localhost:8000/items/99
```

## 📝 Example Usage

```python
# Using Python requests
import requests

# Create an item
response = requests.post("http://localhost:8000/items?item=apple")
print(response.json())  # ["apple"]

# Get item
response = requests.get("http://localhost:8000/items/0")
print(response.json())  # "apple"
```

## 🐛 Error Handling

- **Item not found**: Returns `404` status code with message "Item not found"
- Invalid request: Returns appropriate HTTP error codes

## 📦 Project Structure

```
FAST_API/
├── main.py           # Main FastAPI application
├── README.md         # This file
└── .venv/            # Virtual environment
```

## 🤝 Contributing

Feel free to fork, modify, and improve this project!

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Rahul Singh**

---

**Happy Coding! 🎉**
