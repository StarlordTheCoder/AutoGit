import os
from optparse import OptionParser
from typing import List

from git import Repo, Diff

from automation import Automation
from configurator import Config


class Main:
    @property
    def changed_working_dir(self) -> List[Diff]:
        return self.repo.head.commit.diff(None)

    def check_untracked_files(self):
        for untracked_file in self.repo.untracked_files:
            print(untracked_file)

        for diff in self.changed_working_dir:
            print(str(diff.b_path) + " " + diff.change_type)

    def __init__(self, configuration, repo_path):
        config = Config(configuration)

        self.repo = Repo(repo_path)

        Automation(self.check_untracked_files, 2)

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