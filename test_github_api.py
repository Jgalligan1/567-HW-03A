import unittest
from unittest.mock import patch
from github_api import get_user_repos_and_commits

class TestGitHubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_valid_user(self, mock_get):
        # Mock response for repositories
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        result = get_user_repos_and_commits("richkempinski")
        self.assertIsInstance(result, list)
        if len(result) > 0:
            self.assertIn("repo", result[0])
            self.assertIn("commits", result[0])

    @patch("github_api.requests.get")
    def test_invalid_user(self, mock_get):
        #Simulating an error without actually triggering the error
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {}

        with self.assertRaises(Exception):
            get_user_repos_and_commits("Thisusernamedoesnotexistbecauseitisverylong74747")

    @patch("github_api.requests.get")
    def test_output_format(self,mock_get):
        # Mock repos response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        result = get_user_repos_and_commits("jgalligan1")
        for item in result:
            self.assertIsInstance(item, dict)
            self.assertIn("repo", item)
            self.assertIn("commits", item)

if __name__ == '__main__':
    unittest.main()
