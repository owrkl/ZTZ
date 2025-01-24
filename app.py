from flask import Flask
app = Flask(__name__)
port=8080


@app.route('/')
def hello_world():
    return 'This is ZThon'


if __name__ == "__main__":
    app.run()
