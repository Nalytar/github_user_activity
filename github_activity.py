import sys
import const
import requests
import re as regEx
from EnumEvents import *


class GithubUserActivity:

	def __init__(self, username):
		if regEx.match(const.USERNAME_REGEX, username, regEx.IGNORECASE) is not None:
			print("The Username you provided doesnt fit with the Github ruleset for Usernames.\nCan\'t perform any action... ")
			sys.exit(1)

		self.username = username
		self.activity = self.fetch_user_activity()
		self.activity_sorted = {}

		self.sort_user_activity_by_date()
		self.print_information()

	def fetch_user_activity(self) -> dict:
		response = requests.get( str.replace(const.API_ENDPOINT, const.REPLACE, self.username) )
		if response.status_code == 200:
			return response.json()
		else:
			print("Data fechting failed...")
			return {}

	def sort_user_activity_by_date(self) -> None:
		if self.activity is None or self.activity == {}:
			print("Got no activities!")
			sys.exit(1)

		self.activity_sorted = sorted(self.activity, key=lambda x: x['created_at'])

	def print_information(self) -> None:
		for activity in self.activity_sorted:
			print(f"\t- {EventTypes.get_string_to_print(activity)}")


if __name__ == '__main__':
	# Get Userarguments
	args = sys.argv

	# Check if there are more than 2 (github_activity.py and username)
	if len(args) < 2:
		print("Please provide a username as an argument")
		sys.exit(1)

	# Get the User Activity
	GithubUserActivity(args[1])
