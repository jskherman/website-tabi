+++
title = "📋new_row_on_github_csv.py"
description = "Reading a csv file on GitHub, appending a new row to it, and committing it back again to GitHub. "
date = 2022-11-27
draft = false

[taxonomies]
tags = ["python", "scripting", "csv", "data extraction"]

[extra]
+++

Reading a csv file on GitHub, appending a new row to it, and committing it back again to GitHub.[^1]

```python
# Import packages
import os
import dotenv # For .env files
import datetime
import pandas as pd

# import base64
import requests
import io

# Do `pip install pygithub` first: https://stackoverflow.com/a/50072113
from github import Github
from github import InputGitTreeElement

# dotenv.load_dotenv()

# Make sure to have an environment variable for GitHub authentication
user = os.environ["GITHUB_USERNAME"]
access_token = os.environ["GITHUB_TOKEN"]

# Specify repo and path to CSV file
repo_name = 'your-github-repo-name'
path = 'path-to-file/relative-to/the-root-path/of-the-repo'

# Make GET request for current CSV file
r = requests.get(
    f'https://api.github.com/repos/{user}/{repo_name}/contents/{path}',
    headers={
        'accept': 'application/vnd.github.v3.raw',
        'authorization': f'token {access_token}'
            }
    )

# Convert CSV file to pandas DataFrame
string_io_obj = io.StringIO(r.text)
df = pd.read_csv(string_io_obj)

# Specify contents of the new row in key-value pairs
new_content = {
    "header1": "value1",
    "header2": "value2",
}

# Concatenate new row to df
new_row = pd.DataFrame(new_content, index=[0])
df = pd.concat([df.loc[:],new_row]).reset_index(drop=True)

# Write new version of the CSV file with appended row
df.to_csv(path, index=False)


# --------------------------------------------------------


# user = os.environ["GITHUB_USERNAME"]
# access_token = os.environ["GITHUB_TOKEN"]
# password  = os.environ["GITHUB_PASSWORD"]

# Authenticate with GitHub
g = Github(access_token)
# Get Repository
# repo_name = 'your-github-repo-name'
repo = g.get_user().get_repo(repo_name)

# Save path to current working directory
work_dir = os.getcwd()
# Add file_names relative to the root
file_names = ["test_data.csv"]
file_list = []

# Directory separator
if os.name == "nt": # Windows
    separator = "\\"
if os.name == "posix": # Linux/MacOS
    separator = "/"

# Save full-length file paths
for i in range(len(file_names)):
    file_list.append(work_dir + separator + file_names[i])

# Commit Message
commit_message = "Add new row on " + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# Get latest commit refs
main_ref = repo.get_git_ref('heads/main') # on main branch
main_sha = main_ref.object.sha
base_tree = repo.get_git_tree(main_sha)

# Initialize empty list for git elements
element_list = list()

# Populate list
for i, entry in enumerate(file_list):
    with open(entry) as input_file:
        data = input_file.read()
    element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
    element_list.append(element)

# Commit new files
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(main_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
main_ref.edit(commit.sha)

```

[^1]: 👀 Might be useful??? It's not like I'm using a CSV file as a database...
