
````markdown
# If Statements

It's often useful to only run a piece of code **if** a certain condition is true.

The basic structure looks like this:
````
````python
if CONDITION:
    # do some stuff here

Any code after the `if` block may still run, depending on how the function or program is written.


## Example

def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")
````

### What happens here:

* If `boss_health` is greater than 0:

  ```text
  Ganondorf is alive!
  ```
* Otherwise:

  ```text
  Ganondorf is unalive!
  ```

The `return` statement inside the `if` block stops the function from continuing. Without it, the next line would always run.

````python
## Without `return`
def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
    print("Ganondorf is unalive!")
````
If `boss_health > 0`, this version would print both:

```text
Ganondorf is alive!
Ganondorf is unalive!
```

---

## Summary

* Use `if` to check for a condition.
* Indent the code you want to run when the condition is true.
* Use `return` inside functions to **exit early** when needed.

````markdown
# Remember, you can use the == operator to check if two values are equal. For example:
````
````python
is_equal = 5 == 5
# is_equal is True