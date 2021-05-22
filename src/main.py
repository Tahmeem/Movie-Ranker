from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form_post():
    count = 1
    if request.method == 'GET':
        return render_template('index.html', addAgain="added title", count = count)
    elif request.method == 'POST':
        addAnotherField = request.form['add']
        if addAnotherField == "added title":
            count += 1
            return render_template('index.html', addAgain=addAnotherField, count = count)
        else:
            return render_template('index.html',addAgain=addAnotherField, count=0)

if __name__ == "__main__":
    app.run(debug=True)
