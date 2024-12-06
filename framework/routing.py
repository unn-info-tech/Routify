# class RouteRegistry:
#     def __init__(self):
#         self.routes = {}

#     def add_route(self, path, method, handler):
#         if path not in self.routes:
#             self.routes[path] = {}
#         self.routes[path][method] = handler

#     def find_handler(self, path, method):
#         return self.routes.get(path, {}).get(method)
