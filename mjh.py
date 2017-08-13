from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    exec(python mjh2.py)

if __name__ == '__main__':
    app.run()
