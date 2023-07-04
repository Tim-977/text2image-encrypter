from flask import Flask, redirect, render_template, request

from forms.user import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9@K#3jP!2dR$5sF6gV%1hL&8kM4nT7bY*0cX2zQ1wE4'


@app.route('/')
def start():
    return redirect('/encoder')


@app.route('/encoder', methods=['GET', 'POST'])
def login():
    global text
    form = LoginForm()
    if form.validate_on_submit():
        text = str(form.text.data)
        return redirect('/success')
    return render_template('encoder.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html', text=text)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
