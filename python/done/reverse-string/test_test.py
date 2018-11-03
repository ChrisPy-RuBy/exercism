import unittest
from test import reverse


class TestTest(unittest.TestCase):

  def test_empty_string(self):
      self.assertEqual(reverse(''), '')

  def test_no_primes_under_two(self):
      self.assertEqual(reverse(1), [])

  # def nself):
  #     self.assertEqual(reverse(''), '')

if __name__ == '__main__':
  unittest.main()
