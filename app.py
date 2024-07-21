from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/contributors')
def contributors():
    return render_template('contributors.html')

@app.route('/robot')
def robot():
    return render_template('robot.html')

@app.route('/competitions')
def competitions():
    return render_template('competitions.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)