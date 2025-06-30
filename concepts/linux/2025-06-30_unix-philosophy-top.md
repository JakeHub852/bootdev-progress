
---

### `unix-philosophy-top.md`

---

### Unix Philosophy

The **Unix Philosophy** is a timeless set of principles that guide how Unix-like systems and their tools are designed.

---

#### 1. **Write programs that do one thing and do it well.**

Examples:

* `ls`: lists files and directories
* `grep`: searches for text
* `less`: displays text content interactively

Each of these commands has a single, well-defined purpose — no bloat, no overreach.

---

#### 2. **Write programs to work together.**

Programs are designed to be **composable** using pipes (`|`), allowing complex behavior to be built from simple parts.

Example:

```bash
grep "hello" some_file.txt | less
```

* `grep` searches the file
* `less` paginates the results

Together, they form a small, powerful pipeline.

---

#### 3. **Write programs to handle text streams.**

Why? Because **text** is the universal interface of the command line.

* Text streams can be read, piped, redirected, logged, parsed, or reused
* Any CLI tool that can read from stdin and write to stdout can be part of a larger system

This makes shell-based workflows extremely flexible and automatable.

---

### `top` Command

`top` is a **real-time process viewer** for your system — the CLI equivalent of Task Manager (Windows) or Activity Monitor (macOS).

Use it to:

* See which processes are using the most CPU or memory
* Monitor performance bottlenecks
* Spot runaway programs or memory leaks

```bash
top
```

From there, you can:

* Press `q` to quit
* Use `k` to kill a process by PID
* Sort by CPU or memory usage

---
