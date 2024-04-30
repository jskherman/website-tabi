+++
title = "📋Things I always search for when working with Git"
description = "Save the BFG Repo-Cleaner for later for fixing mistakes in Git commit history."
date = 2024-04-25
draft = false

[taxonomies]
tags = ["git", "tools"]

[extra]
+++

Frequently Asked Questions:

<details><summary>How can I remove/delete a large file from the commit history in the Git repository?</summary>

> Use the [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/), a simpler, faster alternative to git-filter-branch, specifically designed for removing unwanted files from Git history.
>
> Carefully follow the [usage instructions](https://rtyley.github.io/bfg-repo-cleaner/#usage). The core part is just this:
> ```bash
> java -jar bfg.jar --strip-blobs-bigger-than 100M my-repo.git
> ```
>
> Any files over 100 MB in size (that aren't in your latest commit) will be removed from your Git repository's history. You can then use `git gc` to clean away the dead data:
>
> ```bash
> git reflog expire --expire=now --all && git gc --prune=now --aggressive
> ```
>
> After pruning, we can force push to the remote repo*
>
> ```bash
> git push --force
> ```
>
> _**Note**_: cannot force push a protect branch on GitHub
>
> The BFG is typically at least [10-50](https://docs.google.com/spreadsheet/ccc?key=0AsR1d5Zpes8HdER3VGU1a3dOcmVHMmtzT2dsS2xNenc#gid=0) times faster than running `git-filter-branch`, and generally easier to use.
>
> Full disclosure: I'm the author of the BFG Repo-Cleaner.
>
> — [_Roberto Tyley_](https://stackoverflow.com/questions/2100907/how-can-i-remove-delete-a-large-file-from-the-commit-history-in-the-git-reposito) (on StackOverflow)

</details>
