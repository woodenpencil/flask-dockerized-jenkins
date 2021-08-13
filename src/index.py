import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello2():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1", debug=True)
