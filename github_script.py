
import requests
import json
from datetime import datetime, timedelta, timezone

# GitHub repository details
repo_owner = "Nileshkishore"
repo_name = "githubapril3"
branch = "main"  # or any branch you're interested in

# Replace "your-token" with your actual token
headers = {"Authorization": "*************"}

url = "https://api.github.com/user"
response = requests.get(url, headers=headers)
print(response.json())
# GitHub API URL to get commits
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits?sha={branch}"

# GitHub API URL for repository details
repo_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

# GitHub API URL for commits
commits_url = f"{repo_url}/commits?sha={branch}"

# GitHub API URL for branches
branches_url = f"{repo_url}/branches"

# GitHub API URL for contributors
contributors_url = f"{repo_url}/contributors"

# Fetch repository details
repo_response = requests.get(repo_url, headers=headers)

if repo_response.status_code == 200:
    repo_data = repo_response.json()
    print(f"Repository Name: {repo_data['name']}")
    print(f"Description: {repo_data['description']}")
    print(f"URL: {repo_data['html_url']}")
    print(f"Created At: {repo_data['created_at']}")
    print(f"Last Updated: {repo_data['updated_at']}")
    print(f"Stars: {repo_data['stargazers_count']}")
    print(f"Forks: {repo_data['forks_count']}")
    print(f"Open Issues: {repo_data['open_issues_count']}")
    print(f"Language: {repo_data['language']}")
else:
    print(f"Failed to fetch repository details. Status code: {repo_response.status_code}")

# Fetch commits from the repository
commits_response = requests.get(commits_url, headers=headers)

if commits_response.status_code == 200:
    commits = commits_response.json()
    print(f"\nLatest Commit Time: {commits[0]['commit']['committer']['date']}")
    print(f"Latest Commit Message: {commits[0]['commit']['message']}")
    print(f"Committer Name: {commits[0]['commit']['committer']['name']}")
else:
    print(f"Failed to fetch commits. Status code: {commits_response.status_code}")

# Fetch branches from the repository
branches_response = requests.get(branches_url, headers=headers)

if branches_response.status_code == 200:
    branches = branches_response.json()
    print(f"\nBranches:")
    for branch in branches:
        print(f"- {branch['name']}")
else:
    print(f"Failed to fetch branches. Status code: {branches_response.status_code}")

# Fetch contributors from the repository
contributors_response = requests.get(contributors_url, headers=headers)

if contributors_response.status_code == 200:
    contributors = contributors_response.json()
    print(f"\nContributors:")
    for contributor in contributors:
        print(f"- {contributor['login']} (Contributions: {contributor['contributions']})")
else:
    print(f"Failed to fetch contributors. Status code: {contributors_response.status_code}")

# Get information about the last commit time and compare with a threshold (e.g., 10 minutes)
if commits_response.status_code == 200:
    latest_commit_time = commits[0]['commit']['committer']['date']
    latest_commit_time = datetime.strptime(latest_commit_time, '%Y-%m-%dT%H:%M:%SZ')
    latest_commit_time = latest_commit_time.replace(tzinfo=timezone.utc)

    # Define the time threshold (e.g., 10 minutes ago)
    time_threshold = datetime.now(timezone.utc) - timedelta(minutes=10)

    if latest_commit_time > time_threshold:
        print(f"\nThere are recent changes in the GitHub repository! ({latest_commit_time})")
    else:
        print(f"\nNo recent changes in the GitHub repository.")
else:
    print(f"Failed to check recent changes. Status code: {commits_response.status_code}")
