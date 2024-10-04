import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from unittest import mock
from const import API_ENDPOINT, REPLACE


def get_input(text):
	return input(text)


def getUsername():
	return get_input('Enter username: ')


class MyTestCase(unittest.TestCase):

	@mock.patch('test_api_call.get_input', return_value='username')
	def test_userInput_and_replaceInEndpoint(self, input):
		username = getUsername()
		self.assertEqual(username, 'username')
		self.assertNotEqual(API_ENDPOINT, str.replace(API_ENDPOINT, REPLACE, username))


if __name__ == '__main__':
	unittest.main()
