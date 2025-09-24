import unittest
from github_api import get_user_repos_and_commits

class TestGitHubApi(unittest.TestCase):

    def test_valid_user(self):
        result = get_user_repos_and_commits("richkempinski")
        self.assertIsInstance(result, list)
        if len(result) > 0:
            self.assertIn("repo", result[0])
            self.assertIn("commits", result[0])

    def test_invalid_user(self):
        with self.assertRaises(Exception):
            get_user_repos_and_commits("thisuserdoesnotexist999999")

    def test_output_format(self):
        result = get_user_repos_and_commits("octocat")
        for item in result:
            self.assertIsInstance(item, dict)
            self.assertIn("repo", item)
            self.assertIn("commits", item)

if __name__ == '__main__':
    unittest.main()
