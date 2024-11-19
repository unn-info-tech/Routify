import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'framework')))

from framework.app import App

# Initialize the application
app = App()

# Define routes
@app.route('/hello', methods=['GET'])
def say_hello(request):
    return '{"message": "Hello, world!"}'

if __name__ == '__main__':
    app.run()
