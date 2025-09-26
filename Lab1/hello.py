from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <p>Hello world, I am a FLASK APP!</p>
    <p>Go to the <a href="/about">About Page</a>.</p>
    <p>Go to the <a href="/contact">Contact Page</a>.</p>
    '''
    
@app.route('/about')
def about():
    return '''
    <p>This is the About Page.</p>
    <p>Go back to the <a href="/">Home Page</a>.</p>
    <a href="https://www.python.org">Python page</a>
    <a href="https://flask.palletsprojects.com/en/stable/">Flask</a>
    '''

@app.route('/contact')
def contact():
    return '''
    <p>This is the Contact Page.</p>
    <p>Go back to the <a href="/">Home Page</a>.</p>
    '''
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
