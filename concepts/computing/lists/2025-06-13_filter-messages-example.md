## Python List Concepts in `filter_messages()` Function

The `filter_messages()` function is a great example that brings together several core concepts from working with Python lists and strings. Below is a breakdown of the key list-related concepts illustrated by this function.

---

### Function Purpose

This function takes a list of chat messages and returns:

1. A list of messages with the word `"dang"` removed.
2. A list of integers representing how many times `"dang"` was removed from each message.

---

### The Code

```python
def filter_messages(messages):
    filtered_messages = []
    words_removed = []
    for message in messages:
        words = message.split()
        new_words = []
        removed = 0
        for word in words:
            if word == "dang":
                removed += 1
            else:
                new_words.append(word)
        filtered_messages.append(" ".join(new_words))
        words_removed.append(removed)

    return filtered_messages, words_removed
```

---

### Key List Concepts Covered

#### 1. **List Initialization**

Creating empty lists to store results:

```python
filtered_messages = []
words_removed = []
```

#### 2. **Looping Through Lists**

Using a `for` loop to process each message in the input list:

```python
for message in messages:
```

#### 3. **String to List Conversion**

Splitting strings into lists of words:

```python
words = message.split()
```

This is useful for processing text data word by word.

#### 4. **List Construction and Mutation**

Building a new list of words without `"dang"`:

```python
new_words = []
...
new_words.append(word)
```

#### 5. **Conditionals Inside Loops**

Filtering specific items:

```python
if word == "dang":
    removed += 1
else:
    new_words.append(word)
```

#### 6. **List to String Conversion**

Joining a list of words back into a single string:

```python
" ".join(new_words)
```

#### 7. **Appending to Lists**

Storing results in final output lists:

```python
filtered_messages.append(...)
words_removed.append(...)
```

#### 8. **Returning Multiple Lists**

The function returns two separate lists as a tuple:

```python
return filtered_messages, words_removed
```

---

### Example Usage

```python
messages = ["dang it bobby!", "look at it go"]
filtered, removed_counts = filter_messages(messages)
print(filtered)       # ["it bobby!", "look at it go"]
print(removed_counts) # [1, 0]
```

---

### Summary

This function is a great real-world demonstration of how list operations—creation, iteration, conditionals, string manipulation, and return values—can work together to solve a problem in Python. Understanding and practicing these concepts is essential for mastering Python's list capabilities.
