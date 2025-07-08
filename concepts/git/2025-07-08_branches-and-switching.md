
---

### ✅ `2025-07-08_branches-and-switching.md`

````markdown
# Boot.dev – Git Course  
**Date:** July 8, 2025  
**Topic:** Branches & Switching in Git

---

## 🧠 Key Concepts & Notes

- A **branch** is a named pointer to a commit — usually the "tip" of a sequence of commits.
- Creating a branch doesn’t copy your files — it simply creates a new reference, making branches lightweight and cheap.

- Use branches to isolate experimental changes without affecting the main project:
  - Example: trying a new color scheme → work on `color_scheme` branch
  - If it works: merge it into `main`
  - If not: delete the branch safely

- The **default branch** is typically called `main` (previously `master`)
  - GitHub uses `main` by default now
  - It's good practice to follow that convention

- You can rename branches globally and per-repo:
  ```bash
  git config --global init.defaultBranch main
  git branch -m master main
````

* To **create and switch** to a new branch:

  ```bash
  git switch -c branch_name
  ```

* `git switch` is newer and preferred over `git checkout` for branch switching

  * `git switch` is intuitive and clearly signals intent
  * `git checkout` is older and more ambiguous

* Git visualizes branch history as linear or forked paths:

  ```
         G - H    lanes_branch
        /
  ```

A - B - C - D      main

E - F           primes\_branch

````

- Each branch tip moves independently when new commits are made

---

## 💻 Commands Covered

```bash
git branch                  # Show current branch
git switch <branch>        # Switch to an existing branch
git switch -c <branch>     # Create and switch to a new branch
git checkout <branch>      # Older way to switch (still works)
git branch -m old new      # Rename current or given branch
````

---

> *Branches are not copies — they are choices about where to go next.*

````

