````markdown
---

# Bitwise `&` Operator in Python

Bitwise operators are similar to logical operators, but they work **on individual bits** of integers rather than entire boolean values.

## What is a Bitwise AND?

The bitwise **AND** operation (`&`) compares two binary numbers **bit by bit**.
It returns `1` only if **both** bits in the same position are `1`, otherwise it returns `0`.
````
### Example: `5 & 7`

First, represent the numbers in binary:

```
5 =  0101
7 =  0111
----------
     0101  (result of 5 & 7)
```

So:

```python
5 & 7 == 5
```

### How It Works

The operation happens **column by column**:

| Bit 1 | Bit 2 | Result |
| ----- | ----- | ------ |
| 0     | 0     | 0      |
| 1     | 1     | 1      |
| 1     | 0     | 0      |

These are just logical **AND** operations, applied to each bit.

## Binary Notation in Python

Python uses the prefix `0b` to indicate a binary number.

Examples:

```python
0b0101  # = 5 in decimal
0b0111  # = 7 in decimal
```

## Code Example

```python
binary_five = 0b0101
binary_seven = 0b0111

result = binary_five & binary_seven
print(result)  # Output: 5
```

### Another Example: `5 & 2`

```
5 =  0101
2 =  0010
----------
     0000  (result of 5 & 2)
```

So:

```python
5 & 2 == 0
```

---