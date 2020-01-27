from flask import Flask, render_template, jsonify, request
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method=='POST':
        return 'Form Posted'
    elif request.method == 'GET':
        return render_template('form.html', form=form)




if __name__=="__main__":
    app.run(debug=True)