
---

**`2025-07-13_git-reset-soft-and-hard.md`**

````markdown
# Git: Resetting Commits (Soft & Hard)

## Undoing Changes

One of the biggest advantages of Git is its ability to undo changes. In this lesson, we explored three ways to handle undoing recent work:

### Scenario Setup

On the `update_dune` branch, the intern mistakenly overwrote the entire `titles.md` file.

To simulate this:
```bash
echo "* The Internship" > titles.md
````

(Use `>|` instead of `>` if clobbering is disabled.)

Then:

```bash
git status  # Confirm the file was changed
git add titles.md
git commit -m "J: Overwrote titles.md"
```

---

## `git reset --soft`

* Rolls back to a previous commit
* Keeps changes staged (index)
* Good for "undoing a commit" but *preserving* work

```bash
git log  # Get the I commit hash
git reset --soft <hash>
```

Result:

* Commit J is gone
* `titles.md` is still staged with changes

---

## `git reset --hard`

* Rolls back and **discards all changes**
* Resets working directory + staging area
* **Dangerous:** Data loss is permanent

```bash
git reset --hard <I commit hash>
```

Result:

* All changes since commit I are gone
* `titles.md` is back to its original state
* Use `git status` to confirm

---

## ⚠️ Reset Danger Zone

`git reset --hard` is **permanent**. It wipes out changes that aren’t committed, and even uncommits disappear for good.
If you ever use it on an important file without a backup, it's gone.

Use cautiously — and only when you're absolutely sure.

In Part 2 of the Git course, we’ll learn safer alternatives for undoing changes.

---

## Summary

| Command            | Use Case                                | Keeps Changes? |
| ------------------ | --------------------------------------- | -------------- |
| `git reset --soft` | Uncommit but keep staged changes        | ✅              |
| `git reset --hard` | Revert to old commit and delete changes | ❌              |

```
