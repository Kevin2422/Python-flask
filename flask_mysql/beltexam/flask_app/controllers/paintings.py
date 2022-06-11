
from flask_app import app
from flask_app.models.painting import Painting
from flask_app.models.user import User
from flask import render_template,redirect,request,session,flash
@app.route('/createrender/')
def create_render():
    return render_template('create.html', id = session['id'])

@app.route('/addpainting', methods=['post'])
def process_form():
    print(request.form)
    email = {
        'email': session['email']

    }
    user = User.get_by_email(email)

    data ={
        'user_id' : request.form['user_id'],
        'title' : request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'name': f'{user.first_name} {user.last_name}'

    }
    if Painting.validate_painting(data):
        Painting.add_painting(data)

        return redirect(f'/success/{session["id"]}')
    return redirect('/createrender')
@app.route('/view/<int:id>')
def getapainting(id):
    data = {
    'id': id
}
    painting = Painting.select_painting(data)
    return render_template('view.html', painting = painting)

@app.route('/edit/<int:id>')
def edit_form(id):
    data = {
    'id': id
}
    painting = Painting.select_painting(data)

    return render_template('edit.html', painting = painting, ids = id)

@app.route('/editpainting', methods=['post'])
def processedit_form():
    print(request.form)
    email = {
        'email': session['email']

    }
    user = User.get_by_email(email)

    data ={
        'user_id' : request.form['user_id'],
        'title' : request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'name': f'{user.first_name} {user.last_name}',
        'id': request.form['id']
    }
    if Painting.validate_painting(data):
        Painting.update_painting(data)

        return redirect(f'/success/{session["id"]}')
    return redirect(f'/edit/{request.form["id"]}')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    Painting.delete_painting(data)
    return redirect(f'/success/{session["id"]}')


