from typing import List

from git import Repo, Diff

repo = Repo('C:\\Users\\Pascal\\Source\\AutoGit')

for untracked_file in repo.untracked_files:
    print(untracked_file)


def changedWorkingDir() -> List[Diff]:
    return repo.head.commit.diff(None)

for diff in changedWorkingDir():
    print(str(diff.b_path) + " " + diff.change_type)
