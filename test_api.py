import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def print_response(test_name, response):
    print(f"\n{'='*50}")
    print(f"🧪 {test_name}")
    print(f"{'='*50}")
    print(f"Status: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)

# Test 1: Root endpoint
print_response("1. GET / (Root)", requests.get(f"{BASE_URL}/"))

# Test 2: Create first item
print_response("2. POST /items (Apple)", requests.post(
    f"{BASE_URL}/items",
    json={"name": "Apple", "description": "Fresh red apple", "price": 1.99}
))

# Test 3: Create second item
print_response("3. POST /items (Banana)", requests.post(
    f"{BASE_URL}/items",
    json={"name": "Banana", "description": "Yellow banana", "price": 0.99}
))

# Test 4: List all items
print_response("4. GET /items (All)", requests.get(f"{BASE_URL}/items"))

# Test 5: List with limit
print_response("5. GET /items?limit=1", requests.get(f"{BASE_URL}/items?limit=1"))

# Test 6: Get specific item
print_response("6. GET /items/0", requests.get(f"{BASE_URL}/items/0"))

# Test 7: Update item
print_response("7. PUT /items/0 (Update)", requests.put(
    f"{BASE_URL}/items/0",
    json={"name": "Green Apple", "description": "Fresh green apple", "price": 2.49}
))

# Test 8: Delete item
print_response("8. DELETE /items/0", requests.delete(f"{BASE_URL}/items/0"))

# Test 9: Validation error - missing required field
print_response("9. POST with missing 'name' (Invalid)", requests.post(
    f"{BASE_URL}/items",
    json={"description": "No name", "price": 1.99}
))

# Test 10: Validation error - negative price
print_response("10. POST with negative price (Invalid)", requests.post(
    f"{BASE_URL}/items",
    json={"name": "Invalid", "price": -5.99}
))

# Test 11: Not found error
print_response("11. GET /items/999 (Not Found)", requests.get(f"{BASE_URL}/items/999"))

print(f"\n{'='*50}")
print("✅ API Validation Tests Complete!")
print(f"{'='*50}\n")
