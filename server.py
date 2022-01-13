from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  

    
@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    out = ''
    for i in range(int(num)):
        out += f'{str(word)} '
    return out


if __name__=="__main__":    
    app.run(debug=True)    


