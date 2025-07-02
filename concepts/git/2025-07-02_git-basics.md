# 📘 Boot.dev Git Course Notes

## What is Git?

Git is a distributed version control system (VCS) that developers use to:

* Track code changes over time
* Revert mistakes
* Collaborate with others
* Back up code repositories

It has become the industry standard for VCS due to its power, flexibility, and distributed nature.

## Boot.dev CLI Integration

* The **Boot.dev CLI** is used throughout the course for running tests locally.
* Install the CLI and confirm installation with:

  ```bash
  bootdev --version
  ```
* Login with:

  ```bash
  bootdev login
  ```
* Usage:

  * `bootdev run <id>` — run a local test (debug only)
  * `bootdev run <id> -s` — run and submit for grading (use after confirming correctness)

## Installing Git

* Check if Git is installed:

  ```bash
  git --version
  ```
* If not installed (on Ubuntu/WSL):

  ```bash
  sudo apt install git-all
  ```

## Git Command Syntax

* `<angle brackets>` = required
* `[square brackets]` = optional
* Example:

  ```bash
  mkdir <directory-name>
  ```

## Git Documentation (RTFM)

* Git manuals are accessible with `man`:

  ```bash
  man git
  ```
* Pager shortcuts:

  * `q` = quit
  * `j/k` = scroll
  * `/term` = search
  * `n/N` = next/previous match

## Porcelain vs Plumbing

* **Porcelain (high-level)**: `git status`, `add`, `commit`, `push`, `pull`, `log`
* **Plumbing (low-level)**: `git hash-object`, `commit-tree`, etc.
* Course focuses on porcelain commands but occasionally dips into plumbing.

## Git Config (Global Settings)

* Set your identity:

  ```bash
  git config --global user.name "YourName"
  git config --global user.email "you@example.com"
  ```
* Set default branch:

  ```bash
  git config --global init.defaultBranch master
  ```
* View global config file:

  ```bash
  cat ~/.gitconfig
  ```

## Repositories

* A Git repo = a project directory + `.git` folder
* To create:

  ```bash
  mkdir webflyx
  cd webflyx
  git init
  ```
* Confirm `.git` exists:

  ```bash
  ls -a
  ```

## File States

* `untracked` → not yet staged
* `staged` → added to the index for commit
* `committed` → saved to Git history

Check status:

```bash
git status
```

## Staging

* Add a file to staging:

  ```bash
  git add <file>
  ```

## Commit

* Create a commit:

  ```bash
  git commit -m "Add your message here"
  ```

## Core Git Workflow

* The 3 essential commands:

  ```bash
  git status
  git add <file>
  git commit -m "message"
  ```

## Git Log

* View commit history:

  ```bash
  git log
  ```
* View without pager and limit results:

  ```bash
  git --no-pager log -n 10
  ```
* Commits are identified by hashes (first 7 characters are usually enough)
