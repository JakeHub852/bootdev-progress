````markdown

## Converting Binary
Fantasy Quest needs to migrate old data from strings that look like binary to the integers that the binary strings represent. For example:

"100" -> 4
"101" -> 5
"10010" -> 18
The built-in int() function can convert a binary string to an integer. It takes a second argument that specifies the base of the number (binary is base 2). For example:
````
````python
# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)
# 4
````