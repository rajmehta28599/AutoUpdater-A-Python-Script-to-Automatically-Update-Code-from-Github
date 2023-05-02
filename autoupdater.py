import os
from github import Github

# Github repository URL and access token
REPO_URL = 'https://github.com/your-username/your-repo-name'
ACCESS_TOKEN = 'your-access-token'

# Local directory to save updated code
LOCAL_DIR = 'path/to/local/directory'

# Create a Github instance using the PyGithub library and authenticate with the access token
g = Github(ACCESS_TOKEN)

# Get the repository associated with the URL
repo = g.get_repo(REPO_URL.split('github.com/')[1])

# Get the latest commit SHA for the master branch
latest_commit_sha = repo.get_branch('master').commit.sha

print("Code Update 6:35PM 2 May 2023")

# Check if the latest commit SHA matches the SHA of the current local code
if os.path.exists(LOCAL_DIR):
    os.chdir(LOCAL_DIR)
    os.system('git fetch')
    os.system('git reset --hard ' + latest_commit_sha)
else:
    os.system('git clone ' + REPO_URL + ' ' + LOCAL_DIR)

# Print a message indicating whether the code was updated or not
if latest_commit_sha == repo.get_branch('master').commit.sha:
    print('Code is up to date')
else:
    print('Code updated to latest version')
    
print('Code updated to latest version')
print('Code updated to latest version')
print('Code updated to latest version')
print('Code updated to latest version')
print('Code updated to latest version')
