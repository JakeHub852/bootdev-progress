
---

### ✅ `2025-06-26_viewing-files.md`

```markdown
# 📄 Viewing File Contents in the Shell

> Boot.dev – Learn Linux Course  
> 🗓️ 2025-06-26  
> 📍 Lesson: Files, cat, head, tail, less

---

## 📁 Files

Files are raw binary blobs — could be text, images, or anything. On the CLI, you’ll usually be inspecting **text files** like logs, scripts, configs, or data.

---

## 🐱 `cat` – View File Contents

```bash
cat file1.txt
cat file1.txt file2.txt
````

Prints contents of one or more files directly to the terminal.

---

## 🔼 `head` – First n Lines

```bash
head -n 10 file.txt
```

Defaults to 10 lines if `-n` is omitted.

---

## 🔽 `tail` – Last n Lines

```bash
tail -n 10 file.txt
```

---

## 📖 `less` (Better than `more`)

```bash
less file.txt
less -N file.txt  # show line numbers
```

Interactive viewer:

* Scroll with **Enter** (line-by-line), **Spacebar** (page-by-page), **b** (back), **q** (quit)
* Ideal for **large files**

---

## 📝 Assignment Recap

View a file interactively:

```bash
less /worldbanc/private/transactions/2023.csv
```

* Press Enter/Space to scroll
* Press `q` to quit
* Re-run with line numbers:

```bash
less -N /worldbanc/private/transactions/2023.csv
```

Find and copy line **153**.

---

## 🧠 Notes & Reflections

* `less` makes large file browsing manageable — will definitely use it for logs
* `cat` is useful for quick file checks or chaining with `grep`
* The `-N` flag in `less` is a hidden gem

---

```

