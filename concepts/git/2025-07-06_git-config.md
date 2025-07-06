

---

### 🧠 Concepts Covered

#### 🔹 Git Configuration Layers

* Git settings are stored in **hierarchical config files**:

  * **System:** `/etc/gitconfig` – for all users on the system
  * **Global:** `~/.gitconfig` – for a single user (most common)
  * **Local:** `.git/config` – for a specific repository
  * **Worktree:** `.git/config.worktree` – for special cases involving partial clones

* **Precedence order:** Local > Global > System

  * More specific config overrides more general ones

#### 🔹 Config Key/Value System

* Git configs are made up of `<section>.<key>` = `<value>` pairs

  * Example: `user.name = Jake`, `core.editor = vim`

* Keys can be set using:

  ```bash
  git config [--local|--global] <section.key> "<value>"
  ```

* You can add multiple values for the same key using `--add`

* You can view values using:

  * `git config --list --local`
  * `cat .git/config`
  * `git config --get <key>`

#### 🔹 Editing and Removing Keys

* Remove a single key:

  ```bash
  git config --unset <section.key>
  ```

* Remove **all** instances of a duplicate key:

  ```bash
  git config --unset-all <section.key>
  ```

* Remove an entire section:

  ```bash
  git config --remove-section <section>
  ```

#### 🔹 Miscellaneous Insights

* Git config can technically store **any arbitrary keys**, even if Git itself ignores them
* Unlike most key/value stores, Git allows **duplicate keys**
* Useful for experimenting or storing project-specific metadata

---
