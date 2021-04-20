from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    if os.getenv("FLASK_ENV ") == 'production':
        from waitress import serve
        serve(app, host="0.0.0.0", port=5000, )
    else:
        app.run()
