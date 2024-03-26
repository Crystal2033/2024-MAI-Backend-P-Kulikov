# with open('fileWithHtml.txt', 'r', encoding='utf-8') as f:
#     file_contents = f.read()  # Чтение содержимого файла в строку
# data = f"{file_contents}".encode('utf-8')
def app(environ, start_response):
    data = b"Hello world!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
