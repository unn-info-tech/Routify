import unittest
from framework.app import App


class TestApp(unittest.TestCase):
    def test_route_registration(self):
        app = App()

        @app.route('/hello', methods=['GET'])
        def say_hello(request):
            return 'Hello, world!'

        self.assertIn('/hello', app.routes)
        self.assertIn('GET', app.routes['/hello'])


if __name__ == '__main__':
    unittest.main()
