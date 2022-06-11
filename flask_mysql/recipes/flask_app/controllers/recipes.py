from flask_app import app
from flask_app.models.recipe import Recipe
from flask import render_template,redirect,request,session,flash
from datetime import datetime

@app.route('/create')
def create_recipe():
    return render_template('create.html', id = session['id'])

@app.route('/processrecipe', methods= ['post'])
def process_recipe():
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_created': request.form['date_created'],
        'under_30': request.form['under_30'],
        'user_id': session['id']
    }
    if Recipe.validate_user(data):
        Recipe.insert_recipe(data)
        return redirect(f'/success/{session["id"]}')
    return redirect(f'/success/{session["id"]}')

@app.route('/view/<int:id>')
def view_recipe(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_one_recipe(data)
    return render_template('view.html', recipe = recipe, id = session['id'])
@app.route('/delete/<int:id>')
def delete_recipe(id):
    data = {
        'id': id
    }
    Recipe.delete_one_recipe(data)
    return redirect(f'/success/{session["id"]}')
@app.route('/edit/<int:id>')
def edit_recipe(id):
    data = {
        'id': id
    }
    recipe = Recipe.get_one_recipe(data)
    recipe.date_created = recipe.date_created.strftime('%Y-%m-%dT%H%:%M')
    
    
    return render_template('edit.html', recipe = recipe, id = id, sid = session['id'])
@app.route('/updaterecipe/<int:id>', methods= ['post'])
def update_recipe(id):
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_created': request.form['date_created'],
        'under_30': request.form['under_30'],
        'id': id
        
    }
    if Recipe.validate_user(data):
        Recipe.update_one_recipe(data)
        return redirect(f'/edit/{id}')
    return redirect(f'/edit/{id}')
