import os

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


@app.route('/upload', methods=['GET'])
def upload_form():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    upload_dir = 'uploads'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file.save(os.path.join(upload_dir, file.filename))
    text, file_path = decode()
    try:
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied. Unable to delete '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return f'<h2>{text}</h2>'


@app.route('/download_image')
def download_image():
    image_path = 'static\\output.png'
    filename = 'output.png'
    return send_file(image_path, as_attachment=True, attachment_filename=filename)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
