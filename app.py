from flask import Flask, render_template, request, flash, jsonify

app = Flask(__name__)

books = [
  {
    "id": 1,
    "type": "novel"
  },
  {
    "id": 2,
    "type": "regular"
  },
  {
    "id": 3,
    "type": "fiction"
  }
]

@app.route('/', methods=('GET', 'POST'))
def index():
  return render_template('index.html', books=books)
