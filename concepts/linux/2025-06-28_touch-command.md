
---

````markdown
# ✍️ The `touch` Command

> Boot.dev – Learn Linux Course  
> 🗓️ 2025-06-26  
> 📍 Lesson: Touch – Create or Update Files

---

## 📦 What Does `touch` Do?

The `touch` command **updates the access and modification timestamps** of a file. If the file doesn't exist, it **creates an empty file**.

This makes `touch` a convenient tool for:

- Quickly creating new files
- Ensuring a file exists before using it in a script

---

## 🛠️ Basic Usage

```bash
touch new_file.txt
````

Creates an empty file called `new_file.txt`
(Or just updates timestamps if it already exists)

---

## 📄 Creating Multiple Files at Once

```bash
touch file1.txt file2.txt file3.txt
```

Each listed file will be created if it doesn't exist.

---

## 🤖 Why It’s Useful in Scripts

* Ensures log/output/temp files exist without overwriting contents
* Creates placeholder files safely
* Doesn’t modify file content — only timestamps

---

## 🧠 Notes & Reflections

* Intuitive name — but I didn’t realize it doesn’t modify file contents
* Helpful for scripting setups where you don’t want to `echo > file`
* Will likely use this alongside loops or conditional checks

---
