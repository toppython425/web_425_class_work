from module_08_36 import make_sushi, SushiError, TooFewRiceError, TooMuchRiceError
import unittest


class TestMakeSushi(unittest.TestCase):

    def test_make_sushi(self):
        self.assertEqual(make_sushi('california', 90), 'Ваши суши california готовы!')
        with self.assertRaises(SushiError):
            make_sushi('bismark', 90)
        with self.assertRaises(TooFewRiceError):
            make_sushi('yamato', 40)
        with self.assertRaises(TooMuchRiceError):
            make_sushi('yamato', 110)
