import sys
from automation import Automation
from typing import List
from git import Repo, Diff


class Main:
    @property
    def changed_working_dir(self) -> List[Diff]:
        return self.repo.head.commit.diff(None)

    def check_untracked_files(self):
        for untracked_file in self.repo.untracked_files:
            print(untracked_file)

        for diff in self.changed_working_dir:
            print(str(diff.b_path) + " " + diff.change_type)

    def __init__(self, path):
        self.repo = Repo(path)

        Automation(self.check_untracked_files, 2)


main = Main(sys.argv[1])