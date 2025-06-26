

---

````markdown
# 🖥️ What Is a Terminal? What Is a Shell?

> Boot.dev – Learn Linux Course  
> 🗓️ 2025-06-26  
> 📍 Lesson: Terminal vs Shell

---

## 🖲️ Terminal

Historically, a **terminal** was a physical device — a screen and keyboard used to interact with mainframes.

Today, it refers to a **terminal emulator**:
- A program that lets you type commands in a text-based interface
- It **draws text**, handles **input/output**, but **doesn't process commands**
- The actual logic behind command processing comes from the **shell**

🧠 Analogy:  
The terminal is the **interface**, the shell is the **brain**.

---

## 🐚 Shell

The **shell** is the program that:

1. **Reads** your input
2. **Evaluates** it (often by calling other programs)
3. **Prints** the output
4. **Loops** back for more input (aka: **REPL**)

Common shells:
- `bash` (default for Ubuntu)
- `zsh` (popular on macOS)
- `fish`, `sh`, etc.

---

## 💡 Terminal vs Shell

| Component       | Role                                                  |
|----------------|--------------------------------------------------------|
| Terminal        | Shows a prompt, accepts input, displays output        |
| Shell           | Interprets commands, runs programs, handles scripting |

---

## 🧪 Assignment

Run this in your **WSL Ubuntu shell**:

```bash
expr 123456 + 7890
````

Expected output:

```
131346
```

---

## 🧠 Notes & Reflections

* I’ve definitely used "terminal" and "shell" interchangeably before — nice to separate them cleanly
* The REPL model makes sense now: it’s not just for Python!
* Typing `expr` felt old-school, but cool — it’s just another program the shell calls

---

