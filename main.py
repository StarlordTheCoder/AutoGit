from git import Repo

from automation import Automation
from configurator import ConfigManager


class Main:
    def check_untracked_files(self):
        # TODO use print(self.repo.git.diff(shortstat=True))
        # TODO Consider added, modified and removed files
        # TODO Also consider untracked files?
        swag = self.repo.git.diff(numstat=True).split()
        i = 0
        while i < len(swag):
            print("Lines added in " + swag[i + 2] + ": " + swag[i])
            print("Lines removed in " + swag[i + 2] + ": " + swag[i + 1])
            print("")
            i += 3

    def __init__(self, config_manager, configuration, repo_path):
        config = config_manager.get_config(configuration)

        self.repo = Repo(repo_path)

        Automation(self.check_untracked_files, config.interval)