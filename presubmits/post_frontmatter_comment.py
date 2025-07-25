import os
import json
from github import Github


def post_comment_on_pr():
    """
    Posts a comment on a pull request based on the results of the frontmatter check.
    """
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")

    with open(os.getenv("GITHUB_EVENT_PATH"), "r", encoding="utf-8") as file:
        event = json.load(file)

    if "pull_request" not in event:
        print("No pull request found. Exiting.")
        return

    pr_number = event["pull_request"]["number"]
    github_client = Github(token)
    repo = github_client.get_repo(repo_name)
    pull_request = repo.get_pull(pr_number)

    with open("result.txt", "r", encoding="utf-8") as file:
        result = file.read()

    pull_request.create_issue_comment(result)


if __name__ == "__main__":
    post_comment_on_pr()
