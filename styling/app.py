from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Microsite'
    return render_template('index.html', title=name)

if __name__ == '__main__':
    app.run(debug=True)

