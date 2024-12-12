from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('flask.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    name = request.form.get('name')
    return f"Hello, {name}!" 

if __name__ == '__main__':
    app.run(debug=True)








