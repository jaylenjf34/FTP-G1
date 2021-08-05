import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_shouldfail(self):
        self.assertEqual('true', 'false')

    def test_save_connect(unittest.TestCase):
        save_connect('linux.cs.pdx.edu')
        my_connect = retrieve_connect()
        self.assertEqual('linux.cs.pdx.edu', my_connect)


if __name__ == '__main__':
    unittest.main()
