# 🧾 Linux CLI Cheatsheet

## 🔹 Navigation & Filesystem
| Command                         | Description                                      |
|----------------------------------|--------------------------------------------------|
| `pwd`                            | Print current working directory                  |
| `cd path/to/dir`                | Change to specified directory                    |
| `cd ~`                           | Go to home directory                             |
| `cd ..`                          | Move up one directory                            |
| `ls`                             | List directory contents                          |
| `ls -l`                          | List with detailed info (permissions, owner)     |
| `ls -a`                          | Show hidden files                                |
| `clear`                          | Clear terminal screen                            |

## 📁 Files & Directories
| Command                                   | Description                                         |
|------------------------------------------|-----------------------------------------------------|
| `touch file.txt`                         | Create new empty file                               |
| `mkdir new_dir`                          | Create new directory                                |
| `mv source.txt dest/`                    | Move file to directory                              |
| `mv file.txt newname.txt`                | Rename file                                         |
| `cp file.txt copy.txt`                   | Copy file                                           |
| `cp -R dir new_dir`                      | Copy entire directory                               |
| `rm file.txt`                            | Delete file                                         |
| `rm -r dir`                              | Delete directory and contents                       |

## 📄 File Viewing
| Command                           | Description                              |
|----------------------------------|------------------------------------------|
| `cat file.txt`                   | Print entire file contents               |
| `head -n 10 file.txt`            | Print first 10 lines                     |
| `tail -n 10 file.txt`            | Print last 10 lines                      |
| `less file.txt`                 | View file one screen at a time           |
| `less -N file.txt`              | Same as above, with line numbers         |
| `q`                             | Quit less                                |

## 🔍 Search
| Command                                        | Description                              |
|------------------------------------------------|------------------------------------------|
| `grep "word" file.txt`                         | Search file for exact word               |
| `find . -name "*.txt"`                         | Find all .txt files from current dir     |
| `find path/ -name "*keyword*"`                 | Find files containing keyword in name    |

## 👤 Users & Permissions
| Command                                        | Description                              |
|------------------------------------------------|------------------------------------------|
| `sudo command`                                 | Run command with superuser privileges    |
| `ls -l`                                        | Check file permissions                   |
| `chmod u=rwx,g=,o= file_or_dir`                | Set permissions (user, group, others)    |
| `chmod -R u=rwx,g=,o= dir/`                    | Recursively set permissions              |
| `chown user:group file_or_dir`                | Change file owner (requires `sudo`)      |

## ⚙️ Shell Scripts & Executables
| Command                                        | Description                              |
|------------------------------------------------|------------------------------------------|
| `./script.sh`                                  | Execute a script in current directory    |
| `chmod +x script.sh`                           | Make script executable                   |
| `#!/bin/bash` (or `#!/usr/bin/env bash`)       | Shebang: specifies script interpreter    |

## 🌍 Environment
| Command                             | Description                                        |
|------------------------------------|----------------------------------------------------|
| `name="Jake"`                      | Create local shell variable                        |
| `export NAME="Jake"`               | Create environment variable                        |
| `echo $NAME`                       | Use variable                                       |
| `env`                              | List all environment variables                     |
| `echo $PATH`                       | Show PATH variable (search locations for executables) |
| `export PATH="$PATH:/new/path"`    | Temporarily add directory to PATH                  |
| `source ~/.bashrc`                 | Reload shell config file                           |

## 📝 Shell Config
| File                 | Purpose                              |
|----------------------|--------------------------------------|
| `~/.bashrc`          | Bash shell config (Linux)            |
| `~/.zshrc`           | Zsh shell config (macOS / Zsh users) |

---

