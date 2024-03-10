from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            with open(self.path[1:], 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.endswith('.css'):
            self.send_response(200)
            self.send_header('Content-type', 'text/css; charset=utf-8')
            self.end_headers()
            with open(self.path[1:], 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes("404 Not Found", "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        post_data_bytes = self.rfile.read(content_length)

        post_data_str = post_data_bytes.decode("UTF-8")
        post_data_dict = parse_qs(post_data_str)

        # Отправляем данные обратно клиенту
        response_message = "<h2>Submitted Form Data:</h2>"
        response_message += "<ul>"
        for key, values in post_data_dict.items():
            response_message += f"<li>{key}: {', '.join(values)}</li>"
        response_message += "</ul>"
        self.wfile.write(bytes(response_message, "utf8"))

        # Сохраняем данные в файл
        with open("data.txt", "a", encoding="utf-8") as file:
            for value in post_data_dict.values():
                file.write(value[0] + '\n')

with HTTPServer(('localhost', 80), handler) as server:
    server.serve_forever()
