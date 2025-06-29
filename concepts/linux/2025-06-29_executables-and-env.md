
---

````markdown
# Executables, Shells, and the Environment

## Executable Files

Executable files are just files that contain a program your computer can run. These can be:

- **Compiled programs** (machine code, ready to run)
- **Shell scripts** (text interpreted by a shell or other interpreter)

### Running Executables

You can run a file by typing its path:

```bash
./program.sh
````

* `./` means "in the current directory".
* This prefix is required because your shell doesn't assume the current directory is safe.

## Compiled vs. Interpreted Programs

### Compiled Programs

* Written in languages like **Go, C, or Rust**
* Transformed into machine code before execution
* Run directly by the CPU

### Interpreted Programs

* Written in languages like **Python, JavaScript, Ruby**
* Require an interpreter to execute
* Shell scripts (`.sh`) are interpreted by your shell (e.g., `bash`, `zsh`)

---

## The Shebang (`#!`)

A **shebang** is a special line at the top of a script that tells the system how to execute it.

Example:

```bash
#!/bin/sh
```

Or:

```bash
#!/usr/bin/python3
```

* Tells the system to use `/bin/sh` or `/usr/bin/python3` to run the script.
* Without a shebang, you must manually specify the interpreter when running the script.

---

## Bourne Shells: `sh`, `bash`, and `zsh`

* `sh`: Basic POSIX-compliant shell, minimal features
* `bash`: Bourne Again SHell, most common on Linux
* `zsh`: Z Shell, default on macOS, feature-rich

All are sh-compatible, meaning they can run standard `.sh` scripts.

---

## Shell Configuration Files

Configuration files run every time a shell session starts. They are used to:

* Set environment variables
* Create aliases or functions
* Customize shell behavior

### Common Config Files

| Shell | Config File |
| ----- | ----------- |
| bash  | `~/.bashrc` |
| zsh   | `~/.zshrc`  |

You can view hidden files using:

```bash
ls -a ~
```

---

# Environment Variables

Environment variables are shared across all programs started from the shell.

### View All

```bash
env
```

### Set One

```bash
export NAME="Lane"
echo $NAME
# Lane
```

### Use in a Script

```bash
#!/bin/sh
echo "Hi I'm $NAME"
```

Make executable and run:

```bash
chmod +x introduce.sh
./introduce.sh
# Hi I'm Lane
```

---

# The PATH Variable

`PATH` is a built-in environment variable. It tells your shell where to look for executables.

### View Current PATH

```bash
echo $PATH
```

The output will be a colon-separated list of directories:

```
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

When you type a command like `ls`, the shell checks these directories for a matching executable.

### Adding a Directory to PATH

Temporary (for current session):

```bash
export PATH="$PATH:/my/custom/bin"
```

Permanent (in config file like `.bashrc` or `.zshrc`):

```bash
echo 'export PATH="$PATH:/my/custom/bin"' >> ~/.zshrc
```

Then restart your shell or run:

```bash
source ~/.zshrc
```

---

# Summary

* Use `./program` to run scripts in the current directory
* Add shebangs to scripts so the system knows how to run them
* Use environment variables to pass data to scripts
* Use `PATH` to define where your shell looks for executables
* Add paths to `.bashrc` or `.zshrc` for persistence

```

