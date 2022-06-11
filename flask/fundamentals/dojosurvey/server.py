from crypt import methods
from unicodedata import name
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'this'

@app.route('/')
def show():
    return render_template("index.html")
@app.route('/resultprocess', methods= ['POST'])
def process_results():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['comments'] = request.form['comments']
    print(request.form)
    return redirect('/results')


@app.route('/results')
def show_results():
    return render_template("results.html", session = session)



if __name__=="__main__":    
    app.run(debug=True, port = 5001) 