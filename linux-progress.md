# 🐧 Linux Learning Log

## 2025-06-26 – First Steps

- Created Linux concept folder and began taking structured notes
- Added `2025-06-26_intro-cli-vs-gui.md` (CLI vs GUI concepts)
- Added `2025-06-26_wsl-setup.md` (Installing WSL 2 on Windows)
- Reflected on CLI advantages and the shift away from browser-based learning
- Set up base structure for freeform logging going forward

- Logged `2025-06-26_terminal-vs-shell.md` to clarify the difference between terminal emulators and shells (REPL model clicked)
- Added `2025-06-26_variables-and-history.md` covering shell variables, `history`, clearing the screen, and terminal alternatives
- Practiced variable creation and interpolation (`name="Lane"` → `echo Hello $name`)
- Learned arrow key history navigation and cleared cluttered shells with `clear` and `Ctrl + L`
- Made note of Ghostty, Alacritty, and Windows Terminal but sticking with WSL Ubuntu for now


## 2025-06-28 - Deeper Learning
 - Reviewed:
  - Terminal vs Shell vs REPL
  - Filesystems, file paths (absolute/relative), and navigation
  - File I/O commands: `cat`, `head`, `tail`, `less`
  - File and directory operations: `touch`, `mkdir`, `mv`, `rm`, `cp`
  - Pattern search with `grep` and `find`
  - Users and permissions: ownership, `sudo`, `chmod`, `chown`
  - Executables: `sh` files, `./`, shebang (`#!`)
  - Environment variables: `export`, `env`, and `$PATH`
  - Shell configuration files: `.bashrc`, `.zshrc`, `source`
- Created and organized the following markdowns:
  - `terminal-basics.md`
  - `file-navigation.md`
  - `file-io.md`
  - `users-and-permissions.md`
  - `executables-and-env.md`
  - `shell-config.md`
- All content now structured cleanly inside the `linux/` folder of `bootdev-progress` repo



## 2025-06-30 – Final Phase & Course Completion

* Reviewed earlier concepts on laptop:

  * Variables, history, file operations, users and permissions
  * Standard input/output, environment variables, shell config

* Continued on PC and **completed the rest of the Boot.dev Linux course**, starting from `man` command through to package managers and VS Code

* Added the following markdowns to the `linux/` folder:

  * `manuals-help-flags.md`
  * `streams-and-exit-codes.md`
  * `pipes-processes.md`
  * `unix-philosophy-and-top.md`
  * `package-managers.md`

* Logged a final completion summary (`2025-06-30_completion-summary.md`)

* Linux cheatsheet created for core commands and reference

* Fully structured and self-contained note set for the entire course

* Feeling confident in:

  * Shell stream redirection (`>`, `2>`, `<`)
  * Process management with `ps`, `kill`, `top`, and interrupts
  * Understanding `man`, `--help`, and positional arguments
  * Unix philosophy (programs that do one thing well, work together, and use text streams)
  * Package managers (`apt`, `brew`, `webi`) and PATH awareness

---

