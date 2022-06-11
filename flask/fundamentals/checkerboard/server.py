from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def html():
    return render_template("index.html")
@app.route('/<int:num>/<int:nums>/<string:color1>/<string:color2>')          # The "@" decorator associates this route with the function immediately following
def index(num, nums, color1, color2):
    return render_template("index.html", num=num, nums=nums, color1=color1, color2=color2 )


if __name__=="__main__":
    app.run(debug=True, port = 5001)