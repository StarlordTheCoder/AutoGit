from git import Repo

from automation import Automation


class Main:
    """
    Startet den Automationsprozess
    """

    def check_untracked_files(self):
        """
        Überprüft was sich etwas geändert hat und erstellt falls nötig ein Commit.
        """

        has_exceeded_limit = False

        if len(self.repo.untracked_files) >= self.config.requirements.untracked_files:
            has_exceeded_limit = True
        else:
            git_diff_string = self.repo.git.diff(shortstat=True)

            split_diff = git_diff_string.split(", ")

            print(split_diff)

            if len(split_diff) == 1:
                return

            changed_files = split_diff[0].replace(" files changed", "").replace(" file changed", "")
            if len(split_diff) == 3:
                insertions = split_diff[1].replace(" insertions(+)", "")
                deletions = split_diff[2].replace(" deletions(-)", "")
            else:
                if "insertion" in split_diff[1]:
                    insertions = split_diff[1].replace(" insertions(+)", "")
                    deletions = 0
                else:
                    insertions = 0
                    deletions = split_diff[1].replace(" deletions(-)", "")

            if changed_files and int(changed_files) > self.config.requirements.changed_files:
                has_exceeded_limit = True
            elif insertions and int(insertions) > self.config.requirements.added_lines:
                has_exceeded_limit = True
            elif deletions and int(deletions) > self.config.requirements.removed_lines:
                has_exceeded_limit = True

        if has_exceeded_limit:
            # Falls ein konfiguriertes Limit überschritten wurde, erstelle einen Commit
            self.repo.git.add(A=True)
            self.repo.git.commit(m=self.config.commit_message)

    def __init__(self, config_manager, configuration, repo_path):
        self.config = config_manager.get_config(configuration)

        self.repo = Repo(repo_path)

        # Starten den Timer
        Automation(self.check_untracked_files, self.config.interval)