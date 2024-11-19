from framework.app import App

app = App()

@app.route('/hello', methods=['GET'])
def hello_world(request):
    return '{"message": "Hello, world!"}'

if __name__ == '__main__':
    app.run()
