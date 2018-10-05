[list untracked files](https://stackoverflow.com/a/3801554):

```
git ls-files --others --exclude-standard
```

-----

[see a list of which commits are on one branch but not another](https://stackoverflow.com/a/4207176):

```
git log oldbranch ^newbranch --no-merges
```

-----

[undo a commit](https://stackoverflow.com/a/927386):

```
$ git commit -m "Something terribly misguided"             # (1)
$ git reset HEAD~                                          # (2)
<< edit files as necessary >>                              # (3)
$ git add ...                                              # (4)
$ git commit -c ORIG_HEAD                                  # (5)
```
