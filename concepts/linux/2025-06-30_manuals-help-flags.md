
---

## Man

The `man` command is short for "manual". It's a program that displays the manual for other programs.

I know that manuals and documentation can feel intimidating — that's why there are courses like this one to give you a gentler introduction. That said, manuals and documentation will become more useful to you as you become a more experienced developer. They're not as scary as they seem when you actually take the time to read them.

### Using `man`

The `man` command will only work for programs that it has a manual for, but most built-in commands and Unix programs are supported. You just pass the name of the command as an argument. The most intuitive place to start, of course, is reading the manual's manual:

```bash
# open the man pages for the 'man' command
man man
```

### Searching

Most people don't just read man pages for fun. More often, the manual is used as a reference to quickly look up usage or special flags.

You can search for text in the manual by pressing the `/` key and typing your search, then pressing Enter. Let's try to look up what the `-r` flag does for the `ls` command:

```bash
man ls
# type '/-r' to start searching
# press 'n' to jump to the next result
# press 'N' to go back if you went too far
```

---

## Flags

As you've already seen in this course, some commands accept flags. Flags are options that you can pass to a command to change its behavior.

For example, the `ls` command can take a `-l` flag to show a "long" listing of files:

```bash
ls -l
```

Or the `-a` flag to show "all" files, including hidden files:

```bash
ls -a
```

You can also combine flags:

```bash
ls -al
```

### Conventions

Whether or not a command takes flags, and what those flags are, is up to the developer of the command. That said there are some common conventions:

* Single-character flags are prefixed with a single dash (e.g. `-a`)
* Multi-character flags are prefixed with two dashes (e.g. `--help`)
* Sometimes the same flag can be used with a single dash or two dashes (e.g. `-h` or `--help`)

---

## Positional Arguments

Programming languages have functions, and functions take arguments. For example, this Python function takes two parameters: `xp` and `level`:

```python
def print_player(xp, level):
    print("Player has", xp, "xp and is level", level)

print_player(100, 2)
# Player has 100 xp and is level 2
```

In a shell, commands (programs) can also take arguments. For example, the `cd` command takes a single argument (the directory to change to):

```bash
cd /home/wagslane
```

Other commands might take multiple arguments. For example, the `mv` command takes two arguments: the file to move, and the destination to move it to:

```bash
mv file.txt newfile.txt
```

---

## Help

By convention, most production-ready CLI tools have a "help" option that prints information about how to use the tool. It's usually accessed with one of the following:

* `--help` (flag)
* `-h` (flag)
* `help` (first positional argument)

The "help" output is often easier to parse than a full `man` page. It's usually more of a quick start guide than a full manual.

```bash
ls --help
```

---
