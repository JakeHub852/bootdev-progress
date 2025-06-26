
---

````markdown
# 💡 Variables, History, and Terminals

> Boot.dev – Learn Linux Course  
> 🗓️ 2025-06-26  
> 📍 Lesson: Shell Variables, History, and Terminal Tools

---

## 🧾 Shell Variables

Shells like `bash` and `zsh` support basic programming features like variables, but are optimized for **small tasks and automation**, not full applications.

### ➕ Creating a Variable

```bash
name="Lane"
````

⚠️ No spaces around `=`

### 📤 Using a Variable

```bash
echo $name
# Output: Lane
```

### 🧵 String Interpolation

```bash
echo "Hello $name"
# Output: Hello Lane
```

---

## 🕹️ Shell History

Seeing past commands is useful for scripting, debugging, or just re-running things quickly.

### 🔁 View History

```bash
history
```

This prints a numbered list of past commands.

### ⌨️ Navigate with Arrow Keys

* Press **↑** to scroll backward through past commands
* Press **↓** to move forward toward the latest

Example:

```bash
echo hello
echo world
# Now press ↑ to cycle through those two
```

---

## 🧽 Clearing the Terminal

* Use `clear` or `Ctrl + L` to clean up the screen
  *Note: This doesn’t delete your history.*

---

## 🖥 Terminal Alternatives

You're likely using the **default terminal** (e.g., Ubuntu on WSL), but here are other options:

| Terminal             | Notes                                                                   |
| -------------------- | ----------------------------------------------------------------------- |
| **Windows Terminal** | Modern official WSL-compatible terminal                                 |
| **Ghostty**          | Fast, native, customizable (newer option)                               |
| **Alacritty**        | Speed-focused, highly configurable                                      |
| **VS Code / Zed**    | Built-in terminal in code editors (not recommended here for simplicity) |

> ✅ For this course, stick with a **dedicated terminal**, not one embedded in an editor.

---

## 🧠 Notes & Reflections

* Creating and using variables feels like shell scripting is just stripped-down Python
* Arrow key history recall is already saving me time
* Tempted to explore Ghostty later once I'm deeper in, but sticking with WSL for now

---

