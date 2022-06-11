
# relevant code snippet from server.py

# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(User.get_all())
    return render_template("read.html", users = users)

@app.route('/read', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        
    }
    if not User.validate_user(data):
        print(f'is this working')
        return redirect('/')
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/create')
def create():
    return render_template("create.html")

@app.route('/showuser')
def showuser():
    return render_template("readuser.html")

@app.route('/show', methods= ["POST"])
def show():
    session['ide'] = request.form['ide']
    session['first_name']= request.form['first_name']
    session['last_name']= request.form['last_name']
    session['email'] = request.form['email']
    print(session)

    return redirect("/showuser")
@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template("edit_user.html", user = User.get_one(data))   
@app.route('/user/delete/<int:id>')
def delete_user(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')   

@app.route('/user/update', methods=['POST'])
def update_user():
    User.update(request.form)
    return redirect('/')
