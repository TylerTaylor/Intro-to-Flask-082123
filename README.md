# Intro to Flask

## Flask Overview

- Python framework used to build web applications
- Easy to extend core functionality (Flask-SQLAlchemy for example)

## Setup

1. Run `pipenv install && pipenv shell`
2. Import flask, in `server/app.py`:

```python
from flask import Flask
```

3. Create an instance of the `Flask` class, named `app`:

```python
# server/app.py
from flask import Flask

app = Flask(__name__)
```

4. Configure `app.py` to run as a script, and set debug mode to True which will allow us to see our changes without restarting the server:

```python
from flask import Flask

app = Flask(__name__)

# Routes here

if __name__ == '__main__':
    app.run(port=5555, debug=True)
```

5. Create some routes

6. Run the app one of two ways:
    - `python server/app.py` to run it as a script (with debug mode)
    - `flask run` to run it through flask - if you go this route make sure to configure the environment variables:
        ```python
        export FLASK_APP=app.py
        export FLASK_RUN_PORT=5555

        cd server
        flask run
        ```

### Setting up the DB

```
flask db init
flask db migrate -m "Some message"
flask db upgrade
```