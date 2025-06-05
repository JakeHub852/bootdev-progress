
````markdown
# Python Control Flow: If-Elif-Else

An `if` statement can be followed by:

- Zero or more `elif` ("else if") statements
- An optional `else` statement
````
## Syntax Example

```python
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")
````

## How It Works

1. **`if` statement**:

   * Evaluated first.
   * If `True`, its block runs and the rest (`elif`, `else`) are ignored.

2. **`elif` statements**:

   * Evaluated one by one, in order.
   * The first `True` condition runs its block, and the rest are skipped.

3. **`else` statement**:

   * Optional.
   * Runs only if all previous `if` and `elif` conditions are `False`.

## Summary

* Only one block is executed in an `if-elif-else` chain.
* The order of conditions matters.
* Use `elif` to check multiple exclusive conditions.
* Use `else` as a fallback for when none of the conditions are met.

## If-Else Practice
Here are some basic rules with if/else blocks:

You can't have an `elif` or an `else` without an `if`

You can have an `else` without an `elif`

Use the == operator to check if two values are equal

````python
same = 5 == 6
# same is False

same = 6 == 6
# same is True
````
