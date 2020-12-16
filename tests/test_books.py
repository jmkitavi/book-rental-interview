import unittest
from app import Story1, Story2, Story3

class TestBookCalculation(unittest.TestCase):
  def test_story_one(self):
    number_of_books = 2
    duration = 3
    per_day_rental = 1
    self.assertEqual(Story1(number_of_books, duration).calculate_charge(per_day_rental), 6)


  def test_story_two(self):
    number_of_books = 2
    duration = 3

    self.assertEqual(Story2(number_of_books, duration, 'regular').calculate_charge(), 9)
    self.assertEqual(Story2(number_of_books, duration,'fiction').calculate_charge(), 18)
    self.assertEqual(Story2(number_of_books, duration, 'novel').calculate_charge(), 9)
    
  def test_story_three(self):
    number_of_books = 2
    duration = 3

    self.assertEqual(Story3(number_of_books, duration, 'regular').calculate_charge(),7)
    self.assertEqual(Story3(number_of_books, duration, 'fiction').calculate_charge(),18)
    self.assertEqual(Story3(number_of_books, duration, 'novel').calculate_charge(),27)


if __name__ == '__main__':
    unittest.main()
