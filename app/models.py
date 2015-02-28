from . import db

class Profile(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(80), unique=True)
  lastname = db.Column(db.String(80), unique=True)
  age = db.Column(db.String(3), unique=True)
  sex = db.Column(db.String(6), unique=True)
  image = db.Column(db.String(120), unique=True)
  
  def __init__(self, firstname, lastname, age, sex, image):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.sex = sex
    self.image = image
    
  def __repr__(self):
    return '<Profile %r %r %r %r %r>' % (self.lastname, self.username, self.age, self.sex, self.image)