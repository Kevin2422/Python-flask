from crypt import methods
from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'thisis'

@app.route('/')         
def refresh():
    if 'gold' not in session:
        session['gold'] = 0
        print(session['gold'])
    return render_template("index.html", session = session)
@app.route('/process', methods = (['POST']))
def process():
    print(request.form)
    
    session['property'] = request.form['property']
    if 'activity' not in session:
        session['activity'] = ''
    if request.form['property'] == 'farm':
        count = random.randint(10, 20)
        session['gold'] = int(session['gold']) + count
        session['count'] = count
        session['activity'] = f"<div class = 'greentext'>You gained {session['count']} gold from farm</div>" + session['activity']
    if request.form['property'] == 'cave':
        count = random.randint(5, 10)
        session['gold'] = int(session['gold']) + count
        session['count'] = count
        session['activity'] = f"<div class = 'greentext'>You gained {session['count']} gold from cave</div>" + session['activity']
    if request.form['property'] == 'house':
        count = random.randint(2, 5)
        session['gold'] = int(session['gold']) + count
        session['count'] = count
        session['activity'] = f"<div class = 'greentext'>You gained {session['count']} gold from home</div>" + session['activity']
    if request.form['property'] == 'casino':
        count = random.randint(-50, 50)
        session['gold'] = int(session['gold']) + count 
        session['count'] = count   
        if count >= 0:
            session['activity'] = f"<div class = 'greentext'>You gained {session['count']} gold from the casino</div>" + session['activity']
        if count<= 0:
            session['activity'] = f"<div class = 'redtext'>You lost {session['count']} gold from the casino</div>" + session['activity']
    
    return redirect('/')

@app.route('/reset')
def destroy():
    session.clear()
    return redirect('/')


# try using dictionary with key names of farm and key values of random.randint








if __name__=="__main__":    
    app.run(debug=True, port = 5001) 