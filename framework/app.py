from wsgiref.simple_server import make_server

class Routify:
    def __init__(self):
        self.routes = {}

    def route(self, path, methods=['GET']):
        def decorator(func):
            if path not in self.routes:
                self.routes[path] = {}
            for method in methods:
                self.routes[path][method] = func
            return func
        return decorator

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')
        method = environ.get('REQUEST_METHOD', 'GET')

        if path in self.routes and method in self.routes[path]:
            handler = self.routes[path][method]

            if method == 'POST':
                try:
                    content_length = int(environ.get('CONTENT_LENGTH', 0))
                    body = environ['wsgi.input'].read(content_length).decode() if content_length > 0 else ''
                except (ValueError, KeyError):
                    body = ''
                response = handler(environ, body)
            else:
                response = handler(environ)

            start_response('200 OK', [('Content-Type', 'text/plain')])
            return [response.encode()]
        else:
            start_response('404 Not Found', [('Content-Type', 'text/plain')])
            return [b'Route not found']

app = Routify()

@app.route("/", methods=["GET"])
def home(environ):
    return "Welcome to Routify!"

@app.route("/submit", methods=["POST"])
def submit(environ, body):
    return f"Received POST data: {body}"

@app.route("/greet", methods=["GET", "POST"])
def greet(environ, body=None):
    if environ['REQUEST_METHOD'] == 'POST':
        return f"Hello, POST! You sent: {body}"
    return "Hello, GET!"

if __name__ == "__main__":
    with make_server('', 8000, app) as server:
        print("Serving on http://127.0.0.1:8000...")
        server.serve_forever()
