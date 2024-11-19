def json_response(data, status=200):
    return f'HTTP/1.1 {status} OK\nContent-Type: application/json\n\n{data}'
