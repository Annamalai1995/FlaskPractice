from flask import Flask

app=Flask(__name__)

@app.route("/hai")
def haithere():
    return "Welcome to flask web framework"

@app.route("/greet")
def hellothere():
    return "<h1>Zealous tech corp</h1>"

@app.route("/pass/<data>")
def dataPass(data):
    return "<h2>"+data+"</h2>"

@app.route("/number/<int:data>")
def dataNumPass(data):
    return "<h2>"+str(data*data)+"</h2>"

if __name__ == "__main__":
    app.run(debug=True,port=5000)