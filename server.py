from flask import Flask, redirect, render_template, request, send_file

from forms.user import InputTextForm
from utils import decode, encode

app = Flask(__name__)
app.config['SECRET_KEY'] = '9@K#3jP!2dR$5sF6gV%1hL&8kM4nT7bY*0cX2zQ1wE4'


@app.route('/')
def start():
    return render_template('welcome.html', title='welcome page')


@app.route('/encoder', methods=['GET', 'POST'])
def encoder():
    global text
    log = ''
    form = InputTextForm()
    if form.validate_on_submit():
        text = str(form.text.data)
        log = encode(text)
        return redirect('/download_image')
    return render_template('encoder.html', form=form, title='Encoder', text=log)


@app.route('/decoder', methods=['GET', 'POST'])
def decoder():
    return render_template('decoder.html', title='Decoder')


@app.route('/decoder_success')
def decoder_success():
    text = decode()
    return render_template('decoder_success.html', text=text, title='Decoder success')


@app.route('/download_image')
def download_image():
    image_path = 'static\\output.png'
    filename = 'output.png'
    return send_file(image_path, as_attachment=True, attachment_filename=filename)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
