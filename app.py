from flask import Flask, render_template, request, flash, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MNMjWHAlKq1ou8eJ'

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

charges = {
  'number': [],
  'duration': [],
  'books': [],
  'story_one': {
    "total": 0,
    "number": 0,
  }
}

"""Story 1"""
class Story1:
      
  def __init__(self, number_of_books, duration):
    self.number_of_books = number_of_books
    self.duration = duration
  
  def calculate_charge(self, per_day_rental):
    return self.number_of_books * (self.duration * per_day_rental)




@app.route('/', methods=('GET', 'POST'))
def index():
  if request.method == 'POST':
    req = request.form
    book_type = req.get('book_type') or None
    number_of_books = req.get('number') or None
    book_duration = req.get('duration') or None

    try:
      number_of_books = int(str(number_of_books))
      book_duration = int(str(book_duration))

    except ValueError:
      flash('Both no of books and duration should be integers')

    else:
      charges['books'].append(str(number_of_books) + ' ' + book_type + ' x ' + str(book_duration) + ' days')
      charges['number'].append(str(number_of_books) + book_type)
      charges['duration'].append(str(book_duration))

      story_one = Story1(int(number_of_books), int(book_duration))
      story_one_charges = story_one.calculate_charge(1)
      charges['story_one']['total'] = charges['story_one']['total'] + story_one_charges

  return render_template('index.html', books=books, charges=charges)