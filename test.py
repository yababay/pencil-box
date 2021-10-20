import unittest
from contextlib import contextmanager
from main import main
from lib.settings import pencil_min_length, pencil_max_length


class TestMain(unittest.TestCase):

    def test_too_many_pencils(self):
        too_long = tuple(range(1000))
        self.assertRaises(ValueError, main, too_long)

    def test_pencil_box_is_a_tuple(self):
        argument_is_not_a_tuple = []
        self.assertRaises(ValueError, main, argument_is_not_a_tuple)

    def test_every_pencil_is_a_tuple(self):
        argument_with_not_a_tuple = (['red', 12, True])
        self.assertRaises(ValueError, main, argument_with_not_a_tuple)

    def test_bad_color_type(self):
        argument_with_bad_color = (12, 12, True),
        self.assertRaises(ValueError, main, argument_with_bad_color)

    def test_bad_length_type(self):
        argument_with_bad_length = ('red', '12', True),
        self.assertRaises(ValueError, main, argument_with_bad_length)

    def test_bad_sharpeness_type(self):
        argument_with_bad_sharpeness = ('red', 12, 1),
        self.assertRaises(ValueError, main, argument_with_bad_sharpeness)

    def test_has_too_long_pencil(self):
        argument_with_too_long_pencil = ('red', pencil_max_length + .001, True),
        self.assertRaises(ValueError, main, argument_with_too_long_pencil)

    def test_has_too_short_pencil(self):
        argument_with_too_short_pencil = ('red', pencil_min_length - .001, True),
        self.assertRaises(ValueError, main, argument_with_too_short_pencil)

    def test_normal_pencils(self):
        argument_is_ok = ('red', 10, True), ('green', 15, False)
        with self.assertNotRaises(ValueError):
            main(argument_is_ok, test=True)

    @contextmanager
    def assertNotRaises(self, exc_type):
        try:
            yield None
        except exc_type:
            raise self.failureException('{} raised'.format(exc_type.__name__))
            

if __name__ == '__main__':
    unittest.main()
