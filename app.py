from flask import Flask, render_template

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

@app.route("/page")
def pagesOne():
    return render_template("hai.html")

@app.route("/numpage/<int:data>")
def dataPagePass(data):
    return render_template("receive.html",myData=(data*data))

if __name__ == "__main__":
    app.run(debug=True,port=5000)