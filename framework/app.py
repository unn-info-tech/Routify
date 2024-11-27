from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

class App:
    def __init__(self):
        self.routes = {}  

    def route(self, path, methods=['GET']):
        def decorator(func):
            for method in methods:
                if path not in self.routes:
                    self.routes[path] = {}
                self.routes[path][method] = func
            return func
        return decorator

    def run(self, host='127.0.0.1', port=8000):
        server = HTTPServer((host, port), self._handler())
        print(f"Running on http://{host}:{port}")
        server.serve_forever()

    def _handler(self):
        routes = self.routes
        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self._handle_request('GET')

            def do_POST(self):
                self._handle_request('POST')

            def _handle_request(self, method):
                parsed_path = urlparse(self.path).path
                if parsed_path in routes and method in routes[parsed_path]:
                    handler = routes[parsed_path][method]
                    response = handler(self)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(response.encode())
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'{"error": "Not Found"}')

        return RequestHandler
