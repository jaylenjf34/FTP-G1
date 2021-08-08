import unittest
import pysftp
from src import *
from unittest.mock import patch
import mock


@mock.patch.object(
    target=pysftp,
    attribute='Connection',
    autospec=True,
    return_value=mock.Mock(spec=pysftp.Connection)
)
class TestExamples(unittest.TestCase):
    def test_get(self, mock_sftp_conn):
        host = 'test.edu'
        user = 'testuser'
        password = 'p1a2s3s4w5o6r7d8'
        file = 'test.txt'

        mock_sftp = pysftp.Connection(host, user, password)
        mock_sftp.pwd = '/u/test/'
        mock_sftp.get.return_value = file

        self.assertEqual(get(mock_sftp, file), file)
        mock_sftp.reset_mock()

    def test_get_no_item_found(self, mock_sftp_conn):
        host = 'test.edu'
        user = 'testuser'
        password = 'p1a2s3s4w5o6r7d8'
        file = ''

        mock_sftp = pysftp.Connection(host, user, password)
        mock_sftp.pwd = '/u/test/'

        self.assertEqual(get(mock_sftp, file), 'test.txt',
                         'Could not get the file.')

    def test_login(self, mock_sftp_conn):
        host = 'test.edu'
        user = 'testuser'
        password = 'p1a2s3s4w5o6r7d8'

        mock_sftp = pysftp.Connection(host, user, password)

        mock_sftp_conn.assert_called_with(host, user, password)
