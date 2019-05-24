import csv
import os

from flask import Flask, request, render_template, url_for

from main import process_data

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def _():
    return render_template('index.html', value=None)


@app.route("/result", methods=["GET", "POST"])
def count():
    if request.method == "POST":
        print("hi")
        a = int(request.form["revenues"])
        b = int(request.form["employee"])
        c = int(request.form["tse"])
        d = int(request.form["assets"])
        results = []
        with open("Fortune500beg.csv") as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:  # each row is a list
                results.append(row)
        print(type(results))
        a = process_data(results[1:], [d, c, b, a])
        return render_template('result.html', value=a)


@app.route("/result1", methods=["GET", "POST"])
def calc():
    vector = [float(i) for i in request.form["vector"].split()]
    print(vector)
    target = os.path.join(APP_ROOT, 'uploads/')
    if not os.path.isdir(target):
        os.mkdir(target)
    for upload in request.files.getlist("file"):
        filename = upload.filename
        ext = os.path.splitext(filename)[1]
        if ext != ".csv":
            return "upload file with .csv extention"
        destination = "/".join([target, filename])
        upload.save(destination)
        results = []
        with open(destination) as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:  # each row is a list
                results.append([float(i) for i in row])
                print([float(i) for i in row])
        a = process_data(results, vector)

        return render_template('result.html', value = a)


if __name__ == "__main__":
    app.run(debug=True)

