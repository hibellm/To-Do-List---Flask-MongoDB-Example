from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    os.system("python ../semdmail4.py")

if __name__ == '__main__':
    app.run()
