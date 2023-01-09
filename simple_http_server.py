# импортируем классы
from http.server import HTTPServer, BaseHTTPRequestHandler

# где будет запускаться наш сервер
APP_HOST = 'localhost'   # или 127.0..0.1
APP_PORT = 80


class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)  # статус
        self.send_header("Content-type", "text/html; charset=utf-8")  # header
        self.end_headers()

    def _html(self, message):
        content = (f'<html>'
                   f'<body>'
                   f'<h1>{message}</h1>'
                   f'</body>'
                   f'</html>')
        return content.encode("utf8")  # кодируем

    def do_GET(self):
        self._set_headers()  # какие заголовки должны быть в запросе
        message = "Санёчек приветствует всех!"
        self.wfile.write(self._html(message))  # преобразовать в html-код


def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler): # класс сервера и обработчик GET запросов
    server_address = (APP_HOST, APP_PORT)
    # инициализация сервера
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()  # хранить вечно (пока не упадет или не будет отключен)


if __name__ == '__main__':
    # запуск сервера
    run_server(handler_class=SimpleGetHandler)
