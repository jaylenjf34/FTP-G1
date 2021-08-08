import unittest
from src import *
import pysftp
from os.path import exists


class TestFeatures(unittest.TestCase):


    def test_get(self):
        print('Testing get')
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
        SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        get(sftp,'readme.txt')
        self.assertTrue(os.path.exists('r'))
        os.remove('r')

    def test_get_should_fail(self):
        print('Testing get failure')
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
        SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        self.assertEqual(-1, get(sftp,'cool.txt'))
        os.remove('c')

    def test_cwd(self):
        print('Testing cwd')
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
        SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        result = sftp.pwd
        our_result = cwd(sftp)
        self.assertTrue(result == our_result)

    def test_rm_should_fail(self):
        print('Testing rm')
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
        SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        self.assertEqual(-1, rm(sftp,'cool.txt'))

    def test_rename_should_fail(self):
        print('Testing rename')
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
        SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        self.assertEqual(-1, rename(sftp,'cool.txt'))

    def test_remove_directory_should_fail(self):
        print('Testing remove')
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
        SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        self.assertEqual(-1, rmdir(sftp,'spazz'))

    def test_put_should_fail(self):
        print('Testing put')
        SFTP_NET = 'test.rebex.net'
        SFTP_USER = 'demo'
        SFTP_PSWD = 'password'
        sftp = pysftp.Connection(
        SFTP_NET, username=SFTP_USER, password=SFTP_PSWD)
        self.assertEqual(-1, put(sftp,'doxxed'))
