from flask import Flask, render_template, jsonify, request, flash
from forms import ContactForm
from flaskext.mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'development key'
mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com" #gmail smtp settings
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "your_email"
app.config["MAIL_PASSWORD"] = "your_password"

mail.init_app(app)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method=='POST':
        if form.validate()== False:
            flash("all Field are required.")
            return render_template('form.html', form=form)
        else:
            return 'Form Posted'
    elif request.method == 'GET':
        return render_template('form.html', form=form)




if __name__=="__main__":
    app.run(debug=True)