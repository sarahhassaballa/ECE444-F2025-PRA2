# Example 2-1 & 2-2
'''from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run()
'''
#Example 3-4
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#Example 3-11
from flask_moment import Moment
#Example 3-13
from datetime import datetime
#Example 4-2
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired
#Example 4-6
from flask import Flask, render_template, session, redirect, url_for, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm (FlaskForm): 
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email?', validators=[DataRequired()]) 
    submit = SubmitField('Submit')

#Example 4-6
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    name = None
    email = None

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        old_name = session.get('name')
        old_email = session.get('email')

        if old_name and old_name != name:
            flash('Looks like you have changed your name!')

        if old_email and old_email != email:
            flash('Looks like you have changed your email!')

        # Save name and email regardless of validity
        session['name'] = name
        session['email'] = email
        session['submitted'] = True

        return redirect(url_for('index'))

    # Only show name/email if form was submitted this visit
    name = session['name'] if session.get('submitted') else None
    email = session['email'] if session.get('submitted') else None

    return render_template('index.html', current_time=datetime.utcnow(),
                           form=form, name=name, email=email)





#Example 3-13 
#@app.route('/')
#def index():
#    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name, current_time=datetime.utcnow())
    
#Example 3-6
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()