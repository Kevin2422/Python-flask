from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:num>/<string:color>')          # The "@" decorator associates this route with the function immediately following
def index(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port = 5001)    # Run the app in debug mode.