# pylint: disable=import-error
"""
This script posts a comment on a pull request or push event based on the results of a gitleaks scan.

It uses the GitHub API to create comments on pull requests or associated commits
to notify users about potential secrets detected in the repository.
"""

import os
import json
import sys
from github import Github


def post_comment_on_pr():
    """
    Posts a comment on a pull request or push event based on gitleaks scan results.

    The function reads the GitHub event payload to determine whether the event is a pull request
    or a push. It then retrieves the gitleaks scan results from a file and posts a comment
    on the relevant pull request or commit.
    """
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")

    print("Environment Variables:")
    print(f"GITHUB_TOKEN: {token}")
    print(f"GITHUB_REPOSITORY: {repo_name}")
    print(f"GITHUB_EVENT_PATH: {os.getenv('GITHUB_EVENT_PATH')}")

    with open(os.getenv("GITHUB_EVENT_PATH"), "r", encoding="utf-8") as file:
        event = json.load(file)

    if "pull_request" in event:
        pr_number = event["pull_request"]["number"]
    elif "head_commit" in event:
        github_client = Github(token)
        repo = github_client.get_repo(repo_name)
        commits = event["commits"]
        pr_number = None
        for pr in repo.get_pulls(state="open"):
            for commit in commits:
                if pr.head.sha == commit["id"]:
                    pr_number = pr.number
                    break
            if pr_number:
                break
        if not pr_number:
            print("No associated pull request found for the push event. Exiting.")
            return
    else:
        print("No pull request or push event found. Exiting.")
        return

    github_client = Github(token)
    repo = github_client.get_repo(repo_name)
    pull_request = repo.get_pull(pr_number)

    with open("secrets.txt", "r", encoding="utf-8") as file:
        result = file.read()

    print("Contents of secrets.txt:")
    print(result)

    leaks_found = "Potential" in result

    if leaks_found:
        print("LEAKS FOUND")
        comment_body = f"Checked in secrets detected!:\n```\n{result}\n```"
    else:
        print("No leaks found!")
        comment_body = "No checked in secrets detected."

    pull_request.create_issue_comment(comment_body)

    if leaks_found:
        sys.exit(1)


if __name__ == "__main__":
    post_comment_on_pr()
