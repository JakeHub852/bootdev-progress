
---

### ✅ `2025-06-26_filesystem-and-paths.md`

````markdown
# 🌳 Understanding the Filesystem & Paths

> Boot.dev – Learn Linux Course  
> 🗓️ 2025-06-26  
> 📍 Lesson: Filesystem, Absolute & Relative Paths

---

## 📂 What Is a Filesystem?

A **filesystem** organizes all data on your machine into a **tree of files and directories**:

- **Directories** (or folders) hold files and other directories
- **Files** are just blobs of binary data (text, images, videos, etc.)
- The **root** directory is the top of this hierarchy: `/`

Your **current working directory** is usually your home directory on terminal startup.

---

## 🗺️ Filepaths

Run:

```bash
pwd
````

This outputs your **current absolute path**, e.g.:

```
/home/jake
```

Breakdown:

* `/` → root directory
* `home` → subdirectory of root
* `jake` → subdirectory of `home`

---

## 🔼 Parent Directory (`..`)

Use `..` to navigate **up one level** in the directory tree:

```bash
cd ..
```

---

## 🧭 Relative vs Absolute Paths

### Example Directory Tree:

```
vehicles/
└── cars/
    └── fords/
        └── mustang.txt
```

### Relative Path (depends on where you are):

* From `vehicles`: `cars/fords/mustang.txt`
* From `cars`: `fords/mustang.txt`
* From `fords`: `mustang.txt`

### Absolute Path (starts at root):

```
/vehicles/cars/fords/mustang.txt
```

✅ Both relative and absolute paths can refer to the same file — use what’s appropriate based on context.

---

## 🧠 Notes & Reflections

* Relative paths are easier to write when you know where you are
* Absolute paths are more explicit, better for instructions/scripts
* Navigating up and down using `cd`, `pwd`, and relative jumps feels intuitive so far

---

