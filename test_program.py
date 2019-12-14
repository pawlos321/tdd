import unittest
import moj_program

class Test1TDD(unittest.TestCase):

  def test_100(self):
    wynik = moj.program.zwroc_100()
    self.assertEqual(100, wynik)

if __name__== '__main__':
  unittest.main()
