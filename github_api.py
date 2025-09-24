import requests

def get_user_repos_and_commits(username):
    """
    Given a GitHub username, return a list of dictionaries containing
    each repo name and its commit count.
    """
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        raise Exception(f"Failed to fetch repos for user {username}")

    repos = repos_response.json()
    results = []

    for repo in repos:
        repo_name = repo.get("name")
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        if commits_response.status_code != 200:
            commit_count = 0  # fallback if something fails
        else:
            commits = commits_response.json()
            commit_count = len(commits)

        results.append({"repo": repo_name, "commits": commit_count})

    return results


if __name__ == "__main__":
    user = "richkempinski"  # Example user
    repos_and_commits = get_user_repos_and_commits(user)
    for item in repos_and_commits:
        print(f"Repo: {item['repo']} Number of commits: {item['commits']}")
