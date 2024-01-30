from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#使用gunicorn main:app，並不會執行以下的程式
#if __name__ == "__main__":
    #print("Hello World")
    #app.run(host='0.0.0.0',port=5000)

