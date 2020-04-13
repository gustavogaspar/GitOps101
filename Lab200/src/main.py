from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')



# This application is part of the kubernets getting started guide, for more please access:
# https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/