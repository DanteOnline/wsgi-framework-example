# wsgi-framework-example
wsgi-framework-example

## Description

In `main.py` we have simple wsgi framework application.

```python
def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]
```

## Run with gunicorn

```commandline
pip install gunicorn
gunicorn main:application
```

## Run with waitress

```commandline
pip install waitress
python run_waitress.py
```

## Run with python simple server

```commandline
python run_simple.py
```