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

{% toggle(title="How can I remove/delete a large file from the commit history in the Git repository?") %}

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
> The BFG is typically at least [10-50](https://docs.google.com/spreadsheet/ccc?key=0AsR1d5Zpes8HdER3VGU1a3dOcmVHMmtzT2dsS2xNenc) times faster than running `git-filter-branch`, and generally easier to use.
>
> Full disclosure: I'm the author of the BFG Repo-Cleaner.
>
> —[_Roberto Tyley_](https://stackoverflow.com/a/17890278/23523121) (on StackOverflow)

{% end %}

{% toggle(title="How do I remove a submodule?") %}

> In modern Git (I'm writing this in 2022, with an updated `git` installation), this has become quite a bit simpler:
>
>> Run `git rm <path-to-submodule>`, and commit.
>
> This removes the filetree at `<path-to-submodule>`, and the submodule's entry in the `.gitmodules` file. I.e. all traces of the submodule in your repository proper are removed.
>
> As [the docs note](https://git-scm.com/docs/gitsubmodules#:%7E:text=file%20system%2C%20but-,the%20Git%20directory%20is%20kept%20around,-as%20it%20to) however, the `.git` dir of the submodule is kept around (in the `modules/` directory of the main project's `.git` dir), "**to make it possible to checkout past commits without requiring fetching from another repository**".
>
> If you nonetheless want to remove this info, manually delete the submodule's directory in `.git/modules/`, and remove the submodule's entry in the file `.git/config`. These steps can be automated using the commands:
>
> - `rm -rf .git/modules/<path-to-submodule>`
> - `git config --remove-section submodule.<path-to-submodule>`
>
> —[_John Douthat_](https://stackoverflow.com/a/1260982/23523121) (on StackOverflow)

{% end %}
