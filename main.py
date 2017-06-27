import sys
from typing import List
from git import Repo, Diff


class Main:
    @property
    def changedWorkingDir(self) -> List[Diff]:
        return self.repo.head.commit.diff(None)

    def __init__(self, path):
        self.repo = Repo(path)

        for untracked_file in self.repo.untracked_files:
            print(untracked_file)

        for diff in self.changedWorkingDir:
            print(str(diff.b_path) + " " + diff.change_type)


main = Main(sys.argv[1])