#  file name:test_flask-mail.py
import os
from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
app.config.update(
    #  hotmail的設置
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PROT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
)
#  記得先設置參數再做實作mail
mail = Mail(app)


@app.route("/")
def index():
    #  主旨
    msg_title = 'Hello It is Flask-Mail'
    #  寄件者，若參數有設置就不需再另外設置
    msg_sender = 'jasperli0407@gmail.com'
    #  收件者，格式為list，否則報錯
    msg_recipients = ['jasper.lee@bureauveritas.com']
    #  郵件內容
    msg_body = 'Hey, Do you want some coffee?!'
    #  也可以使用html
    msg_html = '<h1>轟隆隆 隆隆隆隆 衝衝衝衝 拉風!</h1>'
    msg = Message(msg_title,
                  sender=msg_sender,
                  recipients=msg_recipients)
    msg.body = msg_body
    msg.html = msg_html
    
    #  mail.send:寄出郵件
    mail.send(msg)
    return 'You Send Mail by Flask-Mail Success!!'

if __name__ == "__main__":
    app.debug = True
    app.run()