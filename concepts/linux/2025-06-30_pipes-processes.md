
---

### `pipes-processes.md`

---

### Piping

One of the most beautiful features of the shell is **piping** — the ability to pass the output of one command directly into another.

#### Pipe syntax: `|`

* Takes **stdout** from the command on the **left**
* Sends it as **stdin** to the command on the **right**

#### Example:

```bash
echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w
# 10
```

In this case:

* `echo` prints the sentence
* `|` sends that output to `wc -w`
* `wc -w` counts the number of words

This works because many commands (like `wc`) can read input directly from stdin.

---

### Interrupting Programs

Sometimes you need to **stop a running program** (hangs, typos, too much output, etc).

Use:

```bash
Ctrl + C
```

This sends a **SIGINT** (interrupt signal) to the program. Most well-behaved programs will terminate when they receive this signal.

---

### Killing Processes

If `Ctrl + C` doesn’t work, you can **forcefully terminate** the program by using:

```bash
kill PID
```

* `PID` = **Process ID**, a unique number for each running process.

#### To find process IDs:

```bash
ps aux
```

* `ps` = process status
* `aux` = show all processes + extended info

#### Tip:

```bash
ps aux | head -n 1
```

This shows the **header row** of the `ps aux` table to help you interpret the output.

---

