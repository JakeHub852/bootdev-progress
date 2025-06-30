
---

### `linux-18-package-managers.md`

---

## 📦 Package Managers & Development Tools

---

### What Is a Package Manager?

A **package manager** is a tool that helps you install, update, and manage software on your system. It handles:

* 📥 Downloading software
* 🧩 Managing dependencies
* 🛠 Installing, updating, and removing software

---

### APT (Ubuntu / WSL)

APT (**Advanced Package Tool**) is the default package manager on Ubuntu (and WSL Ubuntu).

```bash
# Check if APT is installed
apt --version

# Install a package
sudo apt install neovim

# Update package list
sudo apt update

# Upgrade installed packages
sudo apt upgrade
```

---

### Homebrew (macOS)

There is no default package manager on macOS, but **Homebrew** is the de facto standard.

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install a package
brew install neovim

# Update Homebrew and packages
brew update && brew upgrade
```

---

### 📝 Using Neovim (Briefly)

Neovim is a terminal-based text editor. It’s fast and minimal, but has a learning curve.

* Open a file:

  ```bash
  nvim filename.txt
  ```

* **To Exit:**

  * Press `Esc`
  * Then type `:q` (quit), `:w` (write/save), or `:wq` (write and quit)

Neovim is a deep tool — escaping it is your first real victory.

---

### Package Manager Recap

Most package managers follow this pattern:

1. 🕵️ Check for existing installation
2. 🌐 Download from remote repo
3. 📦 Install + resolve dependencies
4. 🔧 Add binaries to `PATH`
5. 🧹 Keep track of versions/locations

---

### Locate Installed Packages

```bash
# Find where a package executable lives
which nvim
```

---

### 🌐 Webi (Optional, Minimalist Installer)

**Webi** allows you to install CLI tools via a web-based script:

* No need for apt/brew
* Run-and-go installer from official sites
* Great for installing single-use tools

---

### 💻 VS Code and Editors

While many developers live in the terminal, others prefer GUI editors. Choose the workflow that suits your brain.

#### Popular GUI Editors:

* **VS Code** (most common)
* Zed
* Cursor
* IntelliJ IDEA

#### Terminal Editors:

* Neovim
* Vim
* Emacs

---

