import unittest
from app import Story1

class TestBookCalculation(unittest.TestCase):
  def test_story_one(self):
    number_of_books = 2
    duration = 3
    per_day_rental = 1
    self.assertEqual(Story1(number_of_books, duration).calculate_charge(per_day_rental), 6)

if __name__ == '__main__':
    unittest.main()
