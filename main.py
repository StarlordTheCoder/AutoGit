from git import Repo

from automation import Automation


class Main:
    def check_untracked_files(self):
        has_exceeded_limit = False

        if len(self.repo.untracked_files) >= self.config.requirements.untracked_files:
            has_exceeded_limit = True
        else:
            git_diff_string = self.repo.git.diff(shortstat=True)

            split_diff = git_diff_string.split(", ")

            print(split_diff)

            changed_files = int(split_diff[0].replace(" files changed", ""))
            insertions = int(split_diff[1].replace(" insertions(+)", ""))
            deletions = int(split_diff[2].replace(" deletions(-)", ""))
            
            if changed_files > self.config.requirements.changed_files or insertions > self.config.requirements.added_lines or deletions > self.config.requirements.removed_lines:
                has_exceeded_limit = True

        if has_exceeded_limit:
            self.repo.git.add(A=True)
            self.repo.git.commit(m=self.config.commit_message)

    def __init__(self, config_manager, configuration, repo_path):
        self.config = config_manager.get_config(configuration)

        self.repo = Repo(repo_path)

        Automation(self.check_untracked_files, self.config.interval)