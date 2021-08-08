import unittest
from src.longlist import *
from src.login import *
from src.changedir import *
from src.cwd import *
from src.mkdir import *
from src.rmdir import *
from src.rename import *
from src.rm import *
from src.logout import *
from src.put import *
from src.put_mutiple import *
from src.get import *
from src.get_multiple import *
from src.chmod import *
from src.lls import *
from src.lpwd import *
from src.lrename import *
from os.path import exists


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

    def test_get(self):
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
            SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        get(sftp,'readme.txt')
        self.assertTrue(exists('FTP-G1/readme.txt'))





    def test_save_connect(unittest.TestCase):
        save_connect('linux.cs.pdx.edu')
        my_connect = retrieve_connect()
        self.assertEqual('linux.cs.pdx.edu', my_connect)


if __name__ == '__main__':
    unittest.main()
