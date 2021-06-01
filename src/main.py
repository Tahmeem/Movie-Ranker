from flask import Flask, render_template, request
import DataWork
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form_post():
    moviePresent = 0
    if request.method == 'GET':
        return render_template('index.html', movies=moviePresent)
    elif request.method == 'POST':
        movieTitles = request.form.getlist('movieName')
        movieDetails = DataWork.storeData(movieTitles)
        moviePresent += 1
        movieDetails = DataWork.printOrder(movieDetails[0],movieDetails[1],movieDetails[2],movieDetails[3],movieDetails[4])
        return render_template('index.html', movies=moviePresent, titles=movieDetails)

if __name__ == "__main__":
    app.run(debug=True)
