from waitress import serve
from main import application


if __name__ == "__main__":
    print("Serving on http://127.0.0.1:8000/")
    serve(application, host="127.0.0.1", port=8000)
