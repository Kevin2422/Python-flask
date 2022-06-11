
from crypt import methods
from flask_app import app
from flask_app.models.user import User
from flask_app.models.painting import Painting
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def homepage():
    
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process_user():
    if request.form['password']:
        print(request.form)
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'password': request.form['password'],
            'c_password': request.form['c_password'],
            'phash': pw_hash
        }
        if not User.validate_user(data):
            return redirect("/")
        User.register_user(data)
        session['fname'] = request.form['fname']
        session['email'] = request.form['email']
        you = User.get_by_email(data)
        session['id'] = you.id
        return redirect(f"/success/{you.id}")
    else:
        data = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'password': request.form['password'],
            'c_password': request.form['c_password'],
            
        }
        if not User.validate_user(data):
            flash('please enter password')
            return redirect("/")
        

@app.route('/success/<int:id>')
def logged_in(id):
    if 'email' not in session:
        flash("Not logged in")
        return redirect('/')
    data = {
        'email': session['email'],
        'id': id

    }

    return render_template('success.html', name = session['fname'], id = id, paintings = Painting.all_painting() )
@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")
@app.route('/login', methods=['post'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    print(user_in_db)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect("/")
    session['fname'] = user_in_db.first_name
    session['email'] =user_in_db.email
    id = user_in_db.id
    session['id'] = user_in_db.id
    return redirect(f"/success/{id}")
    
# @app.route('/createrender/')
# def create_render():
#     return render_template('create.html', id = session['id'])

# @app.route('/addpainting', methods=['post'])
# def process_form():
#     print(request.form)
#     data ={
#         'user_id' : request.form['user_id'],
#         'title' : request.form['title'],
#         'description': request.form['description'],
#         'price': request.form['price']

#     }
#     Painting.add_painting(data)

#     return redirect(f'/success/{session["id"]}')


# @app.route('/send', methods=['post'])
# def send():
#     print(request.form)
#     data = {
#         'name': request.form['how'],
#         'user_id': request.form['id'],
#         'content': request.form['message'],
#         'email': session['email']
#     }
#     User.send_message(data)
#     user_in_db = User.get_by_email(data)
#     id = user_in_db.id
#     return redirect(f'/success/{id}')
# @app.route('/delete', methods = ['post'])
# def delete():
#     print(request.form)
#     data= {
#         'id': request.form['id'],
#         'date_sent': request.form['date_sent']

#     }
#     User.delete_messages(data)
#     return redirect(f'/success/{request.form["id"]}' 