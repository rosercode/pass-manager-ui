from flask import Flask, request, Response, url_for, Blueprint

app = Flask(__name__, static_url_path="/")

if __name__ == '__main__':
    app.run(host='0.0.0.0')