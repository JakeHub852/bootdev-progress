
---

## Inheritance

Inheritance is the “holy grail” of object-oriented programming.

* Non-OOP languages (like Go and Rust) support encapsulation and abstraction.
* Inheritance is typically unique to class-based languages like Python, Java, and Ruby.
* It allows a **child class** to inherit properties and methods from a **parent class**.
* This helps **share code** between classes and avoid repetition.

---

### Example: Aircraft and Helicopter

```python
class Aircraft:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def fly_up(self):
        self.height += self.speed


class Helicopter(Aircraft):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self):
        self.direction += 90
```

* `Helicopter` is a **child class** of `Aircraft`.
* `super()` calls the parent constructor.
* All properties/methods of `Aircraft` are inherited, and new ones (like `rotate`) can be added.

---

### Another Example: Jet

```python
class Jet(Aircraft):
    def __init__(self, speed):
        # Jets always start on the ground
        super().__init__(0, speed)

    def go_supersonic(self):
        self.speed *= 2
```

---

### When to Inherit

Rule of thumb: **A should only inherit from B if A is always a B.**

✔ Correct uses:

* `Cat` inherits from `Animal` (a cat is always an animal).
* `Truck` inherits from `Vehicle`.
* `Lane` inherits from `BadDotaPlayers`.

❌ Incorrect uses:

* `Cat` should not inherit from `Dog`.
* `Animal` should not inherit from `Cat`.
* `Allan` should not inherit from `Employed`.

If you only need to share some functionality:

* Use **shared functions** or
* Create a **new parent class** both can inherit from.

---

### Example: Real Estate

```python
class RealEstate:
    def __init__(self, location):
        self.__location = location


class Residential(RealEstate):
    def __init__(self, location, bedrooms):
        super().__init__(location)
        self.__bedrooms = bedrooms


class House(Residential):
    def __init__(self, location, bedrooms, yard_size):
        super().__init__(location, bedrooms)
        self.__yard_size = yard_size
```

---

### Wide, Not Deep

* Inheritance trees are usually **wide** (one parent, many children) instead of deep.
* Deep inheritance chains (10+ classes) are rare and often a red flag.

**Why wide?**

* A child is a strict subset of its parent.
* Deep trees require children to be “perfect members” of all ancestors, which is unrealistic.
* Wide trees let you create **siblings** that share a base but differ slightly.

---

