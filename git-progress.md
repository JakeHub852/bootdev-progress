

---

# 🔧 Git Learning Log

## 2025-07-02 – Git Setup & First Commits

* Began Git course on Boot.dev
* Created new markdown file: `bootdev-git-course.md` to track all key lessons
* Installed and configured Git:

  * Confirmed Git installed with `git --version`
  * Set global user identity via `git config`
  * Set default branch to `master` using `git config --global init.defaultBranch master`
* Initialized new project repository `webflyx/`

  * Ran `git init` and confirmed `.git` directory created
* Practiced basic Git commands:

  * `git status`: Checked repo state
  * `git add`: Staged files for commit
  * `git commit -m`: Committed changes with descriptive messages
  * `git log`: Viewed commit history with hashes and metadata
* Reinforced Git command syntax and conventions
* Reviewed porcelain vs plumbing command categories
* Reaffirmed RTFM skills via `man git` and practiced navigation/searching

---


## 2025-07-05 – Commit Hashes, Objects, and Git Plumbing

* Continued Git course on Boot.dev, diving into Git internals

* Explored commit hash structure and SHA-1 generation

  * Identified key inputs to a commit hash: message, author, date, and parent commit
  * Learned why identical content can yield different hashes across machines

* Investigated the `.git/objects/` directory structure

  * Used `git log -n 10` to retrieve recent commit hashes
  * Explored subdirectories based on the first two characters of a commit hash
  * Listed and inspected raw Git objects via `ls -al`

* Tried viewing raw commit object with `cat`, confirmed it was unreadable (compressed)

* Used `xxd` to dump the commit file in hex format and redirected to `/tmp/commit_object_hex.txt`

* Introduced `git cat-file -p <hash>` to properly inspect:

  * Commit metadata (tree, author, message)
  * Tree objects and their referenced blobs

* Observed `tree` and `blob` relationships inside Git:

  * Tree = directory snapshot
  * Blob = raw file content

* Created a second commit:

  * Added `titles.md` file
  * Committed with message starting `B:` (e.g. `B: add titles`)
  * Used `git cat-file -p` to inspect new commit — observed additional `parent` field

* Explored Git snapshot behavior:

  * Learned Git stores full file snapshots per commit
  * Confirmed deduplication by checking that unchanged blob hashes remain identical across commits

* Added `quotes/` directory with two new files: `starwars.md` and `dune.md`

  * Committed both in a single commit with message starting `C:`
  * Verified blob hash for `titles.md` stayed the same — unchanged file wasn’t duplicated

* Reinforced difference between porcelain (`git log`) and plumbing (`git cat-file`) commands

* Gained foundational understanding of Git object model and internal storage logic


---

## 2025-07-08 – Branches, Refs, and Git History

* Resumed Git course on Boot.dev after revision break

* Focused on branching concepts, reference pointers, and internal commit history tracking

* Learned that a **branch** is just a lightweight pointer to a specific commit (the "tip")

  * Branches are cheap to create — they don’t duplicate file content
  * Switching between branches moves HEAD to different commit histories

* Renamed default branch to `main` to match modern GitHub convention

  * Updated global config: `init.defaultBranch` → `main`
  * Renamed current branch with `git branch -m master main`

* Created and switched branches using:

  * `git switch -c <branch>` (preferred)
  * Compared to legacy `git checkout` for historical context

* Deepened understanding of **diverging commit history**:

  * Branches can share a base and evolve independently
  * Visualized branching structures using commit diagrams

* Observed how Git logs represent history and refs:

  * Used `git log --oneline`, `--decorate=full`, and `--decorate=no` for clean output
  * Noted how branch tips are visible as refs in log view

* Explored how Git stores branch pointers:

  * Branch refs live in `.git/refs/heads/`
  * Each file contains the commit hash the branch tip currently points to

* Reinforced mental model of Git as a graph of commits and named pointers

* Built confidence in navigating Git history and understanding internal structures


---


# Git Learning Log – 2025-07-11

Today I covered merge concepts in Git, including both standard merge commits and fast-forward merges. I now understand how Git tracks shared history between branches and how to interpret merge graphs. Feeling more confident working with branch workflows and visualizing project history.


---

### ✅ **Git Progress Update – July 12, 2025**

* Practiced branching off older commits using `git switch -c <branch> <commit>`, which is useful for simulating stale branches or isolating test scenarios.
* Revisited the purpose and power of `git rebase` — how it replays commits for a cleaner history without unnecessary merge commits.
* Successfully:

  * Created the `update_dune` branch from an earlier commit.
  * Made two meaningful commits with proper labeling (`H:` and `I:`).
  * Rebased the branch onto `main`, producing a tidy linear commit log.
* Reinforced command fluency with:

  * `git log --oneline`
  * `git rebase main`
  * CLI test runs and branch-specific verification.

**Takeaway:**
Rebase isn't dangerous — it's powerful when used intentionally. Today built more clarity and comfort with foundational branching and history rewriting in Git.


---

### `2025-07-13` – Resetting Changes

* ✅ Completed chapter on `git reset`
* Learned the difference between:

  * `git reset --soft` → undo commit, keep changes staged
  * `git reset --hard` → reset and **discard** changes entirely
* Practiced safely navigating commit history
* Reinforced caution with destructive commands
* +700 XP progress toward daily 1000 XP goal

---

### 📆 2025-07-18 — GitHub Workflow Mastery

- Linked local repo (`webflyx`) to new GitHub remote.
- Practiced full push-pull workflow via GitHub CLI.
- Created and merged a pull request using `add_classics` feature branch.
- Confirmed fast-forward merge on local `main`.
- Reviewed solo vs team Git workflows — now confident in both.
