Project URL: https://roadmap.sh/projects/github-user-activity

# Setup

Use the setup.sh / setup.ps1 to let the script check if python/pip is installed and install all the required packages.
<code>chmod +x setup.sh</code> to provied execute rights for the script

You may need to restart your console after executing the script for the changes to take action
# Github User Activity

Provide the GitHub username as an argument when running the CLI.

<code>github-activity username</code>

Fetch the recent activity of the specified GitHub user using the GitHub API. You can use the following endpoint to fetch the user’s activity:
https://api.github.com/users/{username}/events

Example: https://api.github.com/users/kamranahmedse/events

Display the fetched activity in the terminal.

Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap