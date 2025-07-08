

---

### ✅ `2025-07-08_commits-refs-and-history.md`

```markdown
# Boot.dev – Git Course  
**Date:** July 8, 2025  
**Topic:** Commits, Refs, & Git History

---

## 🧠 Key Concepts & Notes

- Git branches evolve separately after they diverge.
  - Adding a commit on one branch does **not** affect others.
  - This creates a tree-like history with multiple tips.

- Git stores commit history as a chain of snapshots:
````

```
         D    add_classics
        /
```

A - B - C   main

````

- Each commit knows:
- Its parent (except the first/root commit)
- The snapshot of project files at that point

- The **tip of a branch** is the most recent commit it points to.

- Use `git log` to visualize history:
- `--oneline`: compact view
- `--decorate`: shows branch pointers
- `--decorate=full`: shows full refs
- `--decorate=no`: hides refs

Example:
```bash
git log --oneline --decorate=full
````

* Git tracks branches in:

  ```
  .git/refs/heads/
  ```

  Each file here contains the commit hash the branch points to.

* A **ref** is any pointer to a Git object (commits, tags, branches).

  * All branches are refs, but not all refs are branches

---

## 💻 Commands Covered

```bash
git log                     # View commit history
git log --oneline
git log --decorate=full
git log --decorate=no
cat .git/refs/heads/main    # View main branch commit hash directly
```

---

> *A branch is just a name. A commit is a moment. Git lets you name your moments and move between them.*

```

---


