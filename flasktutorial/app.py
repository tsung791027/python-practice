from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] ='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jasperli0407@gmail.com'
app.config['MAIL_PASSWORD'] = 'Tsung791027'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_SENDER'] = 'Jasper Li <jasperli0407@gmail.com>'





db = SQLAlchemy(app)
bootstarp = Bootstrap(app)
migrate = Migrate(app, db)
mail = Mail(app)

#用GET和POST request方法處理表單
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first() #db 在code 操作
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
        form=form, name=session.get('name'),
        known=session.get('known', False))

        #old_name = session.get('name')    ####flash 更換閃現
        #if old_name is not None and old_name != form.name.data:
            #flash('看起來您有更換過您的名字!')
        #session['name'] = form.name.data
        #return redirect(url_for('index'))
    #return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

#自訂錯誤網頁訊息
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return  render_template('500.html'), 500

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.route('/message')
def send_email():
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] ,
                  sender=app.config['FLASKY_SENDER'], recipients=['jasperli0407@gmail.com'])
    #msg.body = render_template(template + '.txt', **kwargs)
    #msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
    return 'You Send Mail by Flask-Mail Success!!'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('submit')


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

if __name__ == '__main__':
    app.run(debug=True)