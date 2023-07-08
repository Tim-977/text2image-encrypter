from flask import Flask, redirect, render_template, request

from forms.user import InputTextForm
from utils import decode, encode

app = Flask(__name__)
app.config['SECRET_KEY'] = '9@K#3jP!2dR$5sF6gV%1hL&8kM4nT7bY*0cX2zQ1wE4'


@app.route('/')
def start():
    return redirect('/encoder')


@app.route('/encoder', methods=['GET', 'POST'])
def encoder():
    global text
    form = InputTextForm()
    if form.validate_on_submit():
        text = str(form.text.data)
        return redirect('/encoder_success')
    return render_template('encoder.html', form=form, title='Encoder')


@app.route('/decoder', methods=['GET', 'POST'])
def decoder():
    return render_template('decoder.html', title='Decoder')


@app.route('/encoder_success')
def encoder_success():
    if encode(text) == 'image saved successfully':
        log = 'image saved successfully'
    else:
        log = 'an error in the encoding function'
    return render_template('encoder_success.html', text=log, title='Encoder success')


@app.route('/decoder_success')
def decoder_success():
    text = decode()
    return render_template('encoder_success.html', text=text, title='Decoder success')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
