
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'thisis'


@app.route('/')         
def refresh():
    
    print(request.form)
    
    if 'increment' not in session:
        session['increment'] = 2
    if 'count' in session:
        temp = int(session['count'])+1
        session['count']= str(temp)
    else:
        session['count'] = '0'
    if 'visit' in session:
        temp = int(session['visit'])+1
        session['visit']= str(temp)
    else:
        session['visit'] = 0
        
        print(session['count'])
        
    return render_template("index.html", request = request.form, session = session)


@app.route('/a')  
def press():
    
    print(request.form)
 
    if 'count' in session and 'increase' in session:
        
        temp = int(session['count']) + int(session['increase']) - 1
        print("temp is :", temp)
        session['count']= str(temp)
        session['increment'] = session['increase']
    elif  'count' in session:
        temp = int(session['count'])+1
        print("temp is :", temp)
        session['count']= str(temp)   
    else:
        session['count'] = '0' 
        
        print(session['count'])
        
    return redirect('/')

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    if request.form['increase'] != '':
        session['increase'] = request.form['increase']
        
        print(session['increase'])
    if 'count' in session and 'increase' in session:
        session['increment'] = session['increase']
    return redirect('/')




if __name__=="__main__":    
    app.run(debug=True, port = 5001) 