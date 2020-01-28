from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter your email."), validators.Email("Please verify your email")])
    subject = TextField("Subject", [validators.Required("Please enter a Subject.")])
    message = TextAreaField("Message", [validators.Required("Please enter a message.")])
    submit  = SubmitField("send")