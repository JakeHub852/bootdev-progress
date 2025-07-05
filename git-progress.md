

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

