
---

# 🧱 Object-Oriented Programming Notes

## Constructors (`__init__`)

Until now, we’ve defined properties at the **class level**, like this:

```python
class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2
```

This works, but in real-world code it’s rare. Instead, we usually define properties inside a **constructor method** called `__init__`.

### Example: Simple Constructor

```python
class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2
```

* `__init__` runs **automatically** when you create an object.
* Properties are tied directly to the instance, not the class.

### Example: Configurable Constructor

```python
class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier_one = Soldier("Legolas", 2, 10)
print(soldier_one.name)        # Legolas
print(soldier_one.armor)       # 2
print(soldier_one.num_weapons) # 10

soldier_two = Soldier("Gimli", 5, 1)
print(soldier_two.name)        # Gimli
```

✅ Constructors make your classes **safer and more flexible**.

---

## Multiple Objects (Instances)

* A class is like a **blueprint** or **template**.
* Each **object (instance)** is a distinct entity with its own data.
* The process of creating an instance is called **instantiation**.

### Example

```python
class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width

wall_maria = Wall(1, 2, 3)
wall_rose = Wall(4, 5, 6)
wall_sina = Wall(9, 8, 7)
```

Each wall is separate — changing one does not affect the others.

---

## Class Variables vs. Instance Variables

### Instance Variables

* Declared inside the constructor (`__init__`).
* Unique to each object.

```python
class Wall:
    def __init__(self):
        self.height = 10

south_wall = Wall()
south_wall.height = 20   # only updates THIS wall
print(south_wall.height) # 20

north_wall = Wall()
print(north_wall.height) # 10
```

---

### Class Variables

* Declared at the top level of a class definition.
* **Shared** between all instances.

```python
class Wall:
    height = 10

south_wall = Wall()
print(south_wall.height)  # 10

Wall.height = 20          # updates ALL instances

print(south_wall.height)  # 20
```

In other languages, these are called **static variables**.

---

### Which Should I Use?

* **Instance variables** are almost always the right choice.
* **Class variables** are like global variables:

  * Harder to track
  * Easy to misuse
  * Can cause bugs if many parts of a program update them

Use class variables only when you **intentionally want shared state**.

---

