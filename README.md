# Routify

Routify is a lightweight Python web framework built for educational purposes.

## Features

- Simple route registration
- GET and POST request handling

## Example

```python
from framework.app import App

app = App()

@app.route('/hello', methods=['GET'])
def hello_world(request):
    return '{"message": "Hello, world!"}'

if __name__ == '__main__':
    app.run()
