import os
import pandas

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from fancyimpute import KNN

from main import process_data

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = set(["csv"])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def _():
    return render_template('index.html', value=None)


@app.route("/result", methods=["GET", "POST"])
def count():
    if request.method == "POST":
        a = request.form["revenues"]
        b = request.form["employee"]
        c = request.form["tse"]
        d = request.form["assets"]
        a = process_data(pandas.read_csv("Fortune500beg.csv"), [d, c, b, a])
        return render_template('result.html', value=a)


@app.route("/result1", methods=["GET", "POST"])
def calc():
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print("folder exist")
    '''
    vector = request.form["vector"].split()

    target = os.path.join(APP_ROOT, 'uploads/')
    if not os.path.isdir(target):
        os.mkdir(target)
    for upload in request.files.getlist("file"):
        filename = upload.filename
        ext = os.path.splitext(filename)[1]
        print(ext)
        if ext != ".csv":
            return "upload file with .csv extention"
        destination = "/".join([target, filename])
        upload.save(destination)
        data = pandas.read_csv(upload)
        train = pandas.DataFrame(KNN(k=5).fit_transform(data))
        a = process_data(train, vector)

        return render_template('result.html', value = a)


if __name__ == "__main__":
    app.run(debug=True)
