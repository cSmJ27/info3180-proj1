from . import db

class Profile(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(80), unique=True)
  lastname = db.Column(db.String(80), unique=True)
  sex = db.Column(db.String(120), unique=True)
  image = db.Column(db.String(120), unique=True)
  
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
  def __repr__(self):
    return '<Profile %r %r>' % (self.lastname, self.username)