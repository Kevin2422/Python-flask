from flask import Flask
app = Flask(__name__)
@app.route('/')         
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def sayDojo():
    return 'Dojo!'
@app.route('/say/<string:name>')
def say(name):
    
    return f'say {name}'
@app.route('/repeat/<int:num>/<string:banana>')
def hellos(num, banana):
    return f'{banana}'* num



if __name__=="__main__":
    app.run(debug=True, port = 5001)