import os
from optparse import OptionParser
from typing import List

from git import Repo, Diff

from automation import Automation
from configurator import Config


class Main:
    def check_untracked_files(self):
        swag = self.repo.git.diff(numstat=True).split()
        # TODO also consider untracked files
        i = 0
        while i < len(swag):
            print("Lines added in " + swag[i + 2] + ": " + swag[i])
            print("Lines removed in " + swag[i + 2] + ": " + swag[i + 1])
            print("")
            i += 3

    def __init__(self, configuration, repo_path):
        config = Config(configuration)

        self.repo = Repo(repo_path)

        Automation(self.check_untracked_files, config.check_interval_seconds)

parser = OptionParser()
parser.add_option("-r", "--repository",
                  dest="repository", help="GIT Repository to use")
parser.add_option("-c", "--config", dest="config",
                  help="Configuration ID to use", metavar="FILE")

(options, args) = parser.parse_args()

configuration = options.config
repository = options.repository

if not configuration:
    # TODO Print available configs
    configuration = input("Configuration: ")

if not repository:
    repository = os.getcwd()

print("Config: " + configuration)
print("Repo: " + repository)

main = Main(int(configuration), repository)