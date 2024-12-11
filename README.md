# Routify

Routify is a lightweight Python web framework inspired by Flask. It allows you to define routes and handle HTTP requests efficiently using a WSGI-compatible application. This framework is designed to demonstrate how web frameworks work under the hood while remaining simple and extensible.

---

## Features

- Route definition with support for multiple HTTP methods (GET, POST, PUT, PATCH, DELETE).
- Lightweight and built on Python's standard `wsgiref` library.
- Easy-to-use decorator for defining routes.
- Supports reading data from request bodies for methods like POST, PUT, and PATCH.
- Extensible architecture to add more features.

---

## Installation

To use Routify, simply clone the repository and ensure you have Python 3.7+ installed.

```bash
git clone https://github.com/unn-info-tech/Routify.git
cd Routify
```
---

## Usage

### 1. Define Routes

Create a `routes.py` file to define your routes:

```python
from framework import Routify

app = Routify()

@app.route("/", methods=["GET"])
def home(environ):
    return "Welcome to Routify!"

@app.route("/submit", methods=["POST"])
def submit(environ, body):
    return f"Received POST data: {body}"
```

### 2. Run the Server

Create an `app.py` file to run the server:

```python
from wsgiref.simple_server import make_server
from framework import Routify

if __name__ == "__main__":
    with make_server('', 8000, app) as server:
        print("Serving on http://127.0.0.1:8000...")
        server.serve_forever()
```

Run the application:

```bash
python framework/app.py
```

Visit your application in the browser at `http://127.0.0.1:8000`.

---

## Testing

You can test the framework using Python's `requests` library. Below is an example test script:

```python
import requests

# Test GET request
response = requests.get("http://127.0.0.1:8000/")
print("GET /:", response.text)

# Test POST request
response = requests.post("http://127.0.0.1:8000/submit", data={'key': 'value'})
print("POST /submit:", response.text)
```

Run the test:

```bash
python test.py
```

---

## Project Structure

```
Routify/
├── framework/
|   ├── framework.py     # Core of the framework
|   ├── routes.py        # Route definitions
|   ├── app.py           # Application entry point  
└── README.md        # Project documentation
└── test.py         # Test script
```

---

## Future Improvements

- Add middleware support.
- Implement a templating engine.
- Add query parameter parsing.
- Support JSON parsing and responses.
- Add session and cookie handling.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
