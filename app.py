from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    movies = pd.read_csv("./static/data.csv")
    return render_template("index.html", movies=movies.to_dict('records'))


if __name__ == '__main__':
    app.run()
