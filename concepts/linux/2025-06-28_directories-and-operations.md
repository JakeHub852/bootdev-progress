
---

````markdown
# 📁 Directories and File Operations

> Boot.dev – Learn Linux Course  
> 🗓️ 2025-06-26  
> 📍 Lesson: `mkdir`, `mv`, `rm`, `cp`, `~`

---

## 📂 What Is a Directory?

A **directory** (aka "folder") is a container in the filesystem that can hold files or other directories. The filesystem forms a nested tree of these containers.

---

## 🏗️ `mkdir` – Make a Directory

Create a new subdirectory inside the current working directory:

```bash
mkdir my_directory
````

---

## 🚚 `mv` – Move or Rename Files

### Rename a File

```bash
mv old_name.txt new_name.txt
```

### Move a File into a Subdirectory

```bash
mv file.txt some_directory/file.txt
```

### Move a File to the Parent Directory

```bash
mv file.txt ../file.txt
```

### Move Without Renaming

```bash
mv file.txt some_directory/
```

> ⚠️ Cannot move a directory into itself or its subdirectories.

---

## 🗑️ `rm` – Remove Files or Directories

### Remove a File

```bash
rm file.txt
```

### Remove a Directory and All Its Contents (Recursive)

```bash
rm -r some_directory
```

> ⚠️ `-r` stands for “recursive” — it will delete all nested contents. Be **very** careful with this.

---

## 📝 `cp` – Copy Files or Directories

### Copy a File

```bash
cp source.txt destination/
```

### Copy a Directory and All Contents

```bash
cp -R my_dir new_dir
```

> `-R` stands for “recursive” — used to copy entire directory trees.

---

## 🏠 Home Directory

Each user has a **home directory**, which contains their personal files and settings.

* It’s where you start when opening a new terminal session
* Safe place to store code, scripts, and config files
* Avoid making changes in system directories like `/etc`, `/bin`, or `/var` unless you know exactly what you're doing

---

### `~` – Home Directory Alias

Instead of typing your full home path, you can use:

```bash
cd ~
```

This always brings you back to your home, no matter where you are.

---

## 🧠 Notes & Reflections

* Learned practical commands for creating, moving, copying, and deleting files
* Really useful to understand how `~` maps to the home directory — makes scripts more portable
* Cautious of `rm -r` now; might alias it with `-i` to prevent accidents

---


```
