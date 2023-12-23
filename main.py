import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
