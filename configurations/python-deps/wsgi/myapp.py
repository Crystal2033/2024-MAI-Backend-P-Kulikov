def app(environ, start_response):
    with open('H-P-Lovecraft.png', 'rb') as f:
        file_contents = f.read()
    data = file_contents
    start_response("200 OK", [
        ("Content-Type", "image/png"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
