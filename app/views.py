"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField, FileField
from wtforms.validators import Required, Email

from app import db
from app.models import Profile


class UserProfileForm(Form):
  firstname = TextField('Firstname', validators=[Required()])
  lastname = TextField('Lastname', validators=[Required()])
  age = IntegerField('Age', validators=[Required()])
  sex = SelectField(choices=[('male', 'Male'), ('female', 'Female')], validators=[Required()])
  image = FileField(u'Image File', validators=[Required()])


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile/', methods=["GET", "POST"])
def add_profile():
  form = UserProfileForm()
  # if it is a post
  if request.method == "POST":
    # check if form was submitted properly
    # use wtforms for that
    # write to the database
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    newProfile = Profile(firstname, lastname)
    db.session.add(newProfile)
    db.session.commit()
    return "{} {} this was a post".format(firstname, lastname)
  return render_template('add_profile.html', form=form)

@app.route('/profiles/')
def list_profiles():
  profiles = Profile.query.all()
  return render_template('list_profiles.html', profiles=profiles)

@app.route('/profile/<int:id>')
def view_profile(id):
  profile = Profile.query.get(id)
  return render_template('view_profile.html', profile=profile)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
