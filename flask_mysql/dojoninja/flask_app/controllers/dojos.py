from crypt import methods
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def homepage():
    print(Dojo.get_all_dojos()) 
    return render_template('index.html', dojos = Dojo.get_all_dojos())

@app.route('/create', methods = ['post'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')

@app.route('/ninja')
def show_ninja_page():

    return render_template('new_ninja.html', dojos = Dojo.get_all_dojos())

@app.route('/create/ninja', methods = ['post'])
def add_ninja():
    data = {
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    if not Ninja.validate_ninja(request.form):
        return redirect('/')
    Ninja.insert_ninja(data)
    return redirect('/')

@app.route('/ninja/<int:id>')
def show_dojo_ninjas(id):
    data=  {
        'id': id
    }
    return render_template('dojoninja.html', dojo = Dojo.get_ninjas_and_dojos(data) )