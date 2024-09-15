from typing import List
import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    movies = _get_records()

    return render_template("index.html", movies=movies)


def _get_records() -> List[object]:
    files = os.listdir('data')
    records = []
    for file_name in files:
        with open(os.path.join('data', file_name), 'r') as f:
            record = json.load(f)
            if 'status_message' not in record.keys():
                records.append(record)
    return records


if __name__ == '__main__':
    app.run()
