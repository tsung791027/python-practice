from . import db

#定義db.model model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    #model relationship
    user = db.relationship('User', backref='role')

def __repr__(self):
    return '<Role %r>' % self.name
#定義db.model user
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # model relationship
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

def __repr__(self):
    return '<User %r>' % self.username