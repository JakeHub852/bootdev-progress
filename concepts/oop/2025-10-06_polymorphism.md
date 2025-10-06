

---

## Polymorphism

Polymorphism is one of the most powerful ideas in object-oriented programming.
It means a **variable, function, or object can take on multiple forms**.

* “Poly” = many
* “Morph” = form

---

### Example

```python
class Creature:
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
```

**Output:**

```
the creature moves
the dragon flies
the kraken swims
```

Each object implements `.move()` differently — but the same method call works for all.
This is **polymorphism** in action.

> “If it looks like a duck, swims like a duck, and quacks like a duck — it’s a duck.”
> In Python, this is known as *duck typing.*

---

## Rectangle Edges

We now work with rectangles instead of single (x, y) points.

### Goal

Implement getter methods for rectangle edges:

* `get_left_x()` → smallest x value
* `get_right_x()` → largest x value
* `get_top_y()` → largest y value
* `get_bottom_y()` → smallest y value

These methods use private coordinates (with `__` prefix) and return the rectangle’s boundary values.
Python’s `min()` and `max()` functions are helpful here.

---

## Overlaps

To determine if two rectangles overlap, all of the following must be true (A = self, B = rect):

* A’s left side ≤ B’s right side
* A’s right side ≥ B’s left side
* A’s top side ≥ B’s bottom side

If all hold true → the rectangles overlap (return `True`).

---

## Dragon Area (Polymorphism in Practice)

The `Unit` class checks if a unit’s *center point* is within an area.
But for large creatures like Dragons, we check if their **hit box** overlaps the area.

### Assignment Summary

#### Dragon class

* Inherit from `Unit`
* Use `super()` to call the parent constructor
* Add dragon-specific parameters
* Create a private `__hit_box` (a `Rectangle` object)
* Override `in_area()`:

  * Build a rectangle from the provided area
  * Use `.overlaps()` to check if the dragon’s hit box overlaps it

#### Hit Box Calculation

```python
x1 = pos_x - width / 2
y1 = pos_y - height / 2
x2 = pos_x + width / 2
y2 = pos_y + height / 2
```

This defines the rectangular “body” of the dragon based on its center position.

---

## Polymorphism Review

* “Poly” = many
* “Morph” = form/change

Polymorphism allows different data types or objects to **share the same interface** (method names and signatures), while each handles behavior differently.

Example: `Shape` → subclasses like `Circle`, `Rectangle`, `Triangle`.

Each implements:

```python
def draw_shape(self):
    ...
```

You can then treat them all as “shapes”:

```python
shapes = [Circle(5, 5, 10), Rectangle(1, 3, 5, 6)]
for shape in shapes:
    print(shape.draw_shape())
```

---

### Function Signatures

A **function signature** includes:

* Function name
* Input parameters
* Return type/output

Example of same signature:

```python
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health
```

Different signature:

```python
class Archer:
    def hit_by_fire(self, dmg):
        self.health -= dmg
        return self.health
```

---

## Operator Overloading

Python allows you to define **custom behavior for standard operators** in your own classes.

Example:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2  # Calls p1.__add__(p2)
```

Result: `p3` is `(6, 8)`

---

### Common Operator Methods

| Operation           | Symbol | Method Name    |          |
| ------------------- | ------ | -------------- | -------- |
| Addition            | `+`    | `__add__`      |          |
| Subtraction         | `-`    | `__sub__`      |          |
| Multiplication      | `*`    | `__mul__`      |          |
| Power               | `**`   | `__pow__`      |          |
| Division            | `/`    | `__truediv__`  |          |
| Floor Division      | `//`   | `__floordiv__` |          |
| Modulo              | `%`    | `__mod__`      |          |
| Bitwise Left Shift  | `<<`   | `__lshift__`   |          |
| Bitwise Right Shift | `>>`   | `__rshift__`   |          |
| Bitwise AND         | `&`    | `__and__`      |          |
| Bitwise OR          | `      | `              | `__or__` |
| Bitwise XOR         | `^`    | `__xor__`      |          |
| Bitwise NOT         | `~`    | `__invert__`   |          |

---

## Overriding Built-in Methods

When printing an object, Python calls `__str__` or `__repr__`.

Default:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(4, 5)
print(p1)  # <Point object at 0xa0acf8>
```

Custom `__str__`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

Output:

```
(4, 5)
```

`__repr__` works similarly but is intended for debugging or developer output.

---

