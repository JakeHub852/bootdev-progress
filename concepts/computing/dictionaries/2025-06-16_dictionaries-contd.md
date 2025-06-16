

````markdown
# Python Dictionaries

## Ordered or Unordered?

As of **Python 3.7**, dictionaries are **ordered**. This means:

- The items have a defined order.
- That order is preserved across iterations.
- You will always get the same order when looping over a dictionary.

In **Python 3.6 and earlier**, dictionaries were **unordered**, meaning:
- Items had no guaranteed order.
- You couldn't rely on their sequence or refer to items by index.

**Takeaway**: If you're using Python 3.7 or later, you can depend on dictionary order.

---

## Nested Dictionaries in Fantasy Quest

Fantasy Quest stores character progress using a nested dictionary structure:

```python
{
    "entity": {
        "character": {
            "name": "Kaladin",
            "quests": {
                "bridge_run": {"status": "In Progress"},
                "talk_to_syl": {"status": "Completed"},
            },
        }
    }
}
````

Each character follows the same structure, with only the values changing. For example:

```python
{
    "entity": {
        "character": {
            "name": "Shallan",
            "quests": {
                "bridge_run": {"status": "Completed"},
                "talk_to_syl": {"status": "In Progress"},
            },
        }
    }
}
```

---

## Merging Dictionaries

When guilds merge in Fantasy Quest, we need to combine two dictionaries.

To merge two dictionaries in Python (with values from the second dict overriding those from the first when keys overlap):

```python
def merge(dict1, dict2):
    return {**dict1, **dict2}
```

### Example:

```python
two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}

merged_dict = merge(two_towers, rotk)
print(merged_dict)
# Output: {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}
```

Note: `Aragorn`'s value was updated from `10` to `100`.

