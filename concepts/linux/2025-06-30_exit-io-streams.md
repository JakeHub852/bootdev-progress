
---

### `exit-io-streams.md`

---

### Exit Codes

Exit codes (sometimes called "return codes" or "status codes") are how programs communicate whether they ran successfully or not.

* `0` is the exit code for **success**.
* Any other code = **error** (usually `1` as a generic failure).

#### Check exit code:

```bash
ls ~
echo $?
# 0

ls /does/not/exist
echo $?
# 1
```

Programs that call other programs often use these codes to decide what to do next (e.g., restart on failure).

---

### Unset Environment Variable

Unset an env variable:

```bash
unset ENV_VAR_NAME
```

Or set it to an empty string:

```bash
export ENV_VAR_NAME=""
```

---

### Standard Output (stdout)

You're already using this — `stdout` is where programs print their **normal output** (default: your terminal).

#### Example in Python:

```python
print("Hello world")
# Hello world
```

#### Example in Shell:

```bash
echo "Hello world"
# Hello world
```

---

### Standard Error (stderr)

A separate stream used for **error messages**. Still goes to terminal by default unless redirected.

#### Example:

```bash
cat doesnotexist.txt
# cat: doesnotexist.txt: No such file or directory
```

---

### Redirecting Output

#### Redirect stdout to a file:

```bash
echo "Hello world" > hello.txt
cat hello.txt
# Hello world
```

#### Redirect stderr to a file:

```bash
cat doesnotexist.txt 2> error.txt
cat error.txt
# cat: doesnotexist.txt: No such file or directory
```

---

### Standard Input (stdin)

Programs can also **read input** from the user or another program.

#### Example in Python:

```python
name = input("What is your name? ")
print("Hello,", name)
# Hello, Lane!
```

#### In Shell:

Use `read` to take input from stdin:

```bash
read name
echo "Hi $name"
```

---

