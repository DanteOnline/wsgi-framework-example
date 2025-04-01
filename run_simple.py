from wsgiref.simple_server import make_server
from main import application


if __name__ == "__main__":
    with make_server("127.0.0.1", 8000, application) as server:
        print("Serving on http://127.0.0.1:8000/")
        server.serve_forever()
