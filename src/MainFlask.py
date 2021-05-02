from flask import Flask, render_template,request

app = Flask(__name__)
numberOfMovies = '0'


@app.route('/',methods = ['GET','POST'])
def form_post():
    if request.method == 'GET':
        return render_template("index.html",count = 0)
    elif request.method == 'POST':
        numberOfMovies = int(request.form['count'])
        return render_template('index.html',count = numberOfMovies)

"""    
@app.route('/')
def printMovies():
    return render_template("index.html", count=countOfMovies)
"""
if __name__ == "__main__":
    app.run(debug=True)
