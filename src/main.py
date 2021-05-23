from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form_post():
    moviePresent = 0
    if request.method == 'GET':
        return render_template('index.html', movies = moviePresent)
    elif request.method == 'POST':
        movieTitles = request.form.get('Names')
        print(movieTitles)
        moviePresent += 1
        print(moviePresent)
        return render_template('index.html', movies=moviePresent, titles=movieTitles)

if __name__ == "__main__":
    app.run(debug=True)
