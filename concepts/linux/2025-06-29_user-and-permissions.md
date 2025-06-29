

---

````markdown
# Users and Permissions

## Users

Unix-like systems support multiple users. Each user has their own:
- Home directory
- Files
- Permissions

Today, most systems are used by a single user, but it's important to understand how multi-user permissions work, especially on servers or shared machines.

## Sudo

- `sudo` stands for **"superuser do"**.
- Allows you to run commands with elevated privileges.
- Requires a password with superuser rights (usually your user password if you're the only user).

⚠️ Be cautious with `sudo`. It can do serious damage to your system if misused.

## Root User

- The **root** user is the ultimate superuser.
- Has access to everything on the system.
- When you run a command with `sudo`, you're effectively executing it as root.

### Example of Dangerous Command

```bash
sudo rm -rf /
````

This command (if not blocked by safeguards) would delete everything on your system. Never run it.

## chown - Change File Ownership

* Use `chown` to change ownership of a file or directory.
* Requires superuser privileges (use with `sudo`).
* Useful when adjusting access control on shared systems.

```bash
sudo chown newuser filename
```

---

# Permissions

Every file and directory has associated permissions represented as a 10-character string:

```
drwxr-xr-x
```

## Breakdown

* First character: Type

  * `d` = directory
  * `-` = file
* Next 9 characters: Permissions, grouped by:

  * Owner
  * Group
  * Others

### rwx Breakdown

* `r` = read
* `w` = write
* `x` = execute

### Examples

| String       | Meaning                                                         |
| ------------ | --------------------------------------------------------------- |
| `-rwxrwxrwx` | A file where **everyone** can read, write, and execute          |
| `-rwxr-xr-x` | A file where **only owner** can write; all can read and execute |
| `drwx------` | A directory where **only owner** has all permissions            |

## chmod - Change Permissions

Use `chmod` to modify permission levels.

```bash
chmod u=rwx,g=,o= file_or_directory
```

* `u` = user (owner)
* `g` = group
* `o` = others
* `=` = sets the specified permission

### Recursive Permission Change

```bash
chmod -R u=rwx,g=,o= private_directory
```

This applies changes to the directory and all its contents.

## View Permissions

```bash
ls -l
```

Use this command to see the permission strings for files and directories in the current location.

```
drwx------  3 user  staff  96 Jun 28  private
```

The first string is what you're looking for: `drwx------`

```
