from flask import Flask, render_template, redirect, request, url_for
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
    context = {}
    context['title'] = 'Microsite'
    context['brand'] = 'Build with flask'
    context['name'] = 'More Templates'
    form = MyForm()

    try:
        with open('text.txt', 'r') as f:
            context['text'] = f.read()
    except:
        context['text'] = ''

    if form.validate_on_submit():
        new_text = request.form['name']
        with open('text.txt', 'a') as f:
            f.write(new_text + '\n')
        return redirect(url_for('index'))

    return render_template('index.html', context=context, form=form)

if __name__ == '__main__':
    app.run(debug=True)

