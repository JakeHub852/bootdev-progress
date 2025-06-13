def reverse_list(items):
    reverse_list = []
    for i in range(len(items)-1, -1, -1):
        reverse_list.append(items[i])
    return reverse_list
"""
Example:
items = [5, 10, 15]
1. len(items)
len(items) gives us the number of elements in the list. Here, it’s 3.

2. The range function
range(start, stop, step) produces numbers from start down to but not including stop, stepping by step.
We use: range(len(items) - 1, -1, -1)

For our example: range(2, -1, -1) produces 2, 1, 0

3. Indexing the list
On each loop, we use items[i] with i from the range:
When i=2, items[2] is 15
When i=1, items[1] is 10
When i=0, items[0] is 5

4. Building the reversed list
We begin with reverse_list = []
Each time through the loop, we append the selected item:
After first loop: [15]
Second: [15, 10]
Third: [15, 10, 5]

5. Return the result
We return reverse_list to get the new, reversed list.
"""