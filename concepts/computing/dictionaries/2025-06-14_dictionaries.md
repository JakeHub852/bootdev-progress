

````markdown
# Python Dictionary Notes

## Dictionaries in Python

Dictionaries in Python are used to store data values in key → value pairs. They are a great way to group related information together.

```python
car = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2019
}
````

---

## Duplicate Keys in Dictionaries

Dictionaries must have unique keys. If the same key is used more than once, the last value assigned to that key will overwrite any previous value.

```python
example = {
  "key": "value1",
  "key": "value2"
}
print(example["key"])  # Output: "value2"
```

---

## Accessing Dictionary Values

You can access values in a dictionary by using the key inside square brackets (`[]`), similar to list indexing but using the key instead of a numeric index.

```python
car = {
    "make": "Toyota",
    "model": "Camry"
}

print(car["make"])  # Output: Toyota
```

---

## Setting Dictionary Values

You can create an empty dictionary and add key-value pairs later. To assign a value to a key, use the assignment operator (`=`) with square brackets.

```python
planets = {}
planets["Earth"] = True
planets["Pluto"] = False

print(planets["Pluto"])  # Output: False
```

---

## Updating Dictionary Values

If you assign a new value to an existing key, the old value is overwritten with the new one.

```python
planets = {
    "Pluto": True,
}
planets["Pluto"] = False

print(planets["Pluto"])  # Output: False
```

---

## Deleting Dictionary Values

You can delete an existing key-value pair from a dictionary using the `del` keyword.

```python
names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["joe"]

print(names_dict)  
# Output: {'jack': 'bronson', 'jill': 'mcarty'}
```

---

## Deleting Keys That Don't Exist

Attempting to delete a key that doesn't exist in the dictionary will raise a `KeyError`.

```python
names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["unknown"]  # KeyError: 'unknown'
```

To avoid this, check if the key exists using the `in` keyword before deleting:

```python
if "unknown" in names_dict:
    del names_dict["unknown"]
```

