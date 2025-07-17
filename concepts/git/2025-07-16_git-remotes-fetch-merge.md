

---

### 📄 `2025-07-16_git-remotes-fetch-merge.md`

````markdown
# Git: Remotes, Fetching & Merging  
**Date:** 2025-07-16  
**XP Earned:** 250  
**Boot.dev Course:** Git

---

## 🧠 Concepts Covered

### 🔹 Git Remotes  
- Remotes are external repos that share some history with our local repo.
- Git is distributed — there's no true "central" repo; GitHub is just someone else's repo.
- By convention, we call our "source of truth" remote `origin`.

### 🔹 Adding a Remote  
```bash
git remote add origin ../webflyx
````

* `origin` points to the original `webflyx` repo from within `webflyx-local`.

### 🔹 Fetching

```bash
git fetch
```

* Downloads all objects and metadata from the remote into our local `.git/objects` directory.
* Before fetching, only 3 entries were present (empty-ish state).

### 🔹 Viewing Remote Logs

```bash
git log origin/update_dune --oneline
```

* Displays commits A–I from the `update_dune` branch on the remote.

### 🔹 Merging Remote Branches Locally

```bash
git merge origin/main
```

* Fast-forward merge brings all commits from `origin/main` into local `main`.
* Confirmed with `git log` that commits now exist locally.

---

## 📁 File/Repo Structure

```
project-root/
├── webflyx/
│   └── (original remote repo)
└── webflyx-local/
    └── (new local repo with origin pointing to ../webflyx)
```

---

## ✅ CLI Tests

All CLI tests run from within `webflyx-local` directory and passed.

---

## 🗒️ Notes

* The concept of distributed version control becomes more real when working with two local repos.
* Fetching does not bring working files — only objects and metadata.
* Merging is what brings remote commits into the working tree.

----
