
---

````markdown
# Boot.dev – Git Course  
**Date:** July 5, 2025  
**Topic:** Git Internals – Hashes, Objects & Plumbing

---

## ✅ Completed Assignments

- [x] Used `git log -n 10` to view recent commit hashes
- [x] Explored `.git/objects/` directory and matched hash folder
- [x] Used `cat` on raw object (confirmed unreadable output)
- [x] Used `xxd` to hex-dump object file and redirected output to `/tmp/commit_object_hex.txt`
- [x] Used `git cat-file -p` to inspect commit object and redirected to `/tmp/catfileout.txt`
- [x] Identified tree hash from commit and inspected it
- [x] Used `git cat-file -p` on blob to retrieve file content and saved to `/tmp/blobfile.txt`
- [x] Created `titles.md` and committed with message starting `B:`
- [x] Verified second commit includes a `parent` field
- [x] Created `quotes/` directory with `starwars.md` and `dune.md`
- [x] Committed both files with message starting `C:`
- [x] Verified that `titles.md` blob hash remained unchanged across commits

---

## 🧠 Key Concepts & Notes

- Commit hashes are derived from:
  - Content
  - Commit message
  - Author name & email
  - Timestamp
  - Parent commit (if any)

- Git uses **SHA-1** to generate a unique 40-character hash for each object  
  → Hash = SHA

- `.git/objects/` contains Git’s low-level data storage:
  - **Tree** = a directory snapshot
  - **Blob** = a file's contents
  - Commit object points to a tree, which points to blobs

- `cat` shows compressed binary output; use `xxd` to inspect the raw file safely

- Use `git cat-file -p <hash>` to pretty-print:
  - Commit: shows author, message, parent (if any), and tree
  - Tree: shows blobs (files) and nested trees (folders)
  - Blob: reveals actual file content

- Git **stores full snapshots**, not diffs — but it:
  - Compresses file content
  - Reuses identical blobs across commits

---

## 💻 Commands Used

```bash
git log -n 10
ls -al .git/objects/
cat .git/objects/<dir>/<file>
xxd .git/objects/<dir>/<file> > /tmp/commit_object_hex.txt
git cat-file -p <hash> > /tmp/catfileout.txt
git cat-file -p <tree-hash>
git cat-file -p <blob-hash> > /tmp/blobfile.txt
git add .
git commit -m "B: add titles"
git commit -m "C: add quotes"
````

---



