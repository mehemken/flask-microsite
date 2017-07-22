from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Form definition
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

# Flask app object
app = Flask(__name__)
app.secret_key = b'm\xb7\x12\x97\xb4\x98\x88~\xf4o'

# Route
@app.route('/', methods=['GET', 'POST'])
def index():
    name = 'Microsite'
    form = MyForm()
    text = ''
    if form.validate_on_submit():
        text = request.form['name']
        return render_template('navbar.html', title=name, form=form, text=text)
    return render_template('navbar.html', title=name, form=form, text=text)

if __name__ == '__main__':
    app.run(debug=True)

