from git import Repo

from automation import Automation


class Main:
    def check_untracked_files(self):
        hasExceededLimit = False

        if len(self.repo.untracked_files) >= self.config.requirements.untracked_files:
            hasExceededLimit = True

        print(self.repo.git.diff(shortstat=True))
        # TODO Consider added, modified and removed files
        if hasExceededLimit:
            self.repo.git.add(A = True)
            self.repo.git.commit(m = self.config.commit_message)

    def __init__(self, config_manager, configuration, repo_path):
        self.config = config_manager.get_config(configuration)

        self.repo = Repo(repo_path)

        Automation(self.check_untracked_files, self.config.interval)