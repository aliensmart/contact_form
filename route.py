from flask import Flask, render_template, jsonify, request, flash
from forms import ContactForm
from flaskext.mail import Mail, Message
import os


app = Flask(__name__)
app.secret_key = 'development key'
mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com" #gmail smtp settings
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get('DB_USER')
app.config["MAIL_PASSWORD"] = os.environ.get('DB_PASS')

mail.init_app(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method=='POST':
        if form.validate()== False:
            flash("all Field are required.")
            return render_template('form.html', form=form)
        else:
            msg = Message(form.subject.data, sender='contact@exemple.com', recipients=[os.environ.get('DB_USER')])   
            msg.body = """
            From: {} <{}>
            {}
            """.format(form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            
    elif request.method == 'GET':
        return render_template('form.html', form=form)




if __name__=="__main__":
    app.run(debug=True)