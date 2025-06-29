

---

````markdown
# 🔎 `grep` and `find` – Searching in the Shell

> Boot.dev – Learn Linux Course  
> 🗓️ 2025-06-28  
> 📍 Lesson: `grep` (search inside files) & `find` (search for files)

---

## 📘 `grep` – Search Inside Files

CLI equivalent of **Ctrl+F**: search text within one or more files.

### 📄 Basic Syntax

```bash
grep "search_term" filename
````

Example:

```bash
grep "hello" words.txt
```

* Prints lines that contain `"hello"`
* **Case-sensitive** by default
* Use `"*"` wildcards with care — grep works on content, not filenames

---

## 💡 Pro Tip: Tab Autocomplete

When typing file or directory names:

* Type the first few letters, then press `Tab`
* Shell autocompletes or lists options
* Huge time-saver when navigating deep paths

---

## 📁 `find` – Search for Files by Name

Unlike `grep`, `find` helps you locate **files and directories** based on names or patterns.

### 🔍 Find a File by Exact Name

```bash
find some_directory -name hello.txt
```

### 🔠 Find by Pattern (Wildcard)

```bash
find some_directory -name "*.txt"
find some_directory -name "*joint*"
```

* `*` = wildcard (matches anything)
* Wrap wildcards in quotes to prevent shell expansion

---

## 🧠 grep vs find

| Command | Searches...              | Example Use Case                         |
| ------- | ------------------------ | ---------------------------------------- |
| `grep`  | **Inside files**         | Find lines that contain "error" in logs  |
| `find`  | **File/directory names** | Locate all `.log` files in a folder tree |

---

## 🧠 Notes & Reflections

* Grep makes CLI search surprisingly powerful — fast once you get used to the syntax
* Wildcards + quotes are crucial with `find`
* Tab autocomplete is low-key life-changing for shell navigation
* Clear now why `grep` ≠ `find` — I’d been conflating them before

---
