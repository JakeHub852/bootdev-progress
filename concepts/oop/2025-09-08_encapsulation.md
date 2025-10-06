

---

# Encapsulation in Python

Encapsulation is the practice of hiding complexity inside a **black box** so that it's easier to focus on the problem at hand.

---

## Functions as Encapsulation

The simplest example of encapsulation is a **function**.
The caller of a function doesn't need to worry about what happens inside — just the inputs and outputs.

```python
# Who even knows how this function works???
# I sure don't, I just call it and assume
# it calculates the acceleration correctly
acceleration = calc_acceleration(initial_speed, final_speed, time)
```

To use the `calc_acceleration` function, we don't need to think about each line of code inside.
We just need to know that if we give it these inputs:

* `initial_speed`
* `final_speed`
* `time`

…it will produce the correct `acceleration` as an output.

---

## Public and Private

By default, all properties and methods in a class are **public**.
That means you can access them with the `.` operator:

```python
wall.height = 10
print(wall.height)
# 10
```

Private data members let us encapsulate logic and data within a class definition.
To make a property or method private, prefix it with **two underscores**:

```python
class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance


front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30
```

We do this to make it easier to use the class.
When another developer (or even ourselves) uses `Wall`, they don’t need to think about how `armor` and `magic_resistance` affect the defense.
They simply call the public `get_defense()` method and trust the correct value will be returned.

---

## Not About Security

Encapsulation is all about **organization** and **ease of use**, not security.

Think of it like this:

* The casing on your computer hides its inner workings,
  but it doesn’t stop you from opening it.
* A filing cabinet keeps things tidy and easy to find,
  but doesn’t prevent anyone from peeking inside.

Encapsulation and the concepts of private/public members have **nothing to do with security**.
They just make code easier to work with.

---

## Encapsulation in Python

Python is very dynamic, so it relies on **convention** rather than strict enforcement.

* Prefixing with `__` is a **strong suggestion** that you shouldn’t touch it.
* But… if a developer wants to break convention, they *can*.

```python
class Wall:
    def __init__(self, height):
        # the double underscore makes this a private property
        # but it's not strictly enforced, there are hacks to get around it
        self.__height = height

    def get_height(self):
        return self.__height
```

---

## Key Takeaways

* Encapsulation = **hiding complexity in a black box**.
* Makes code **easier to use** and **organize**.
* Private members in Python (`__var`) are **convention, not security**.
* Always provide clear **public methods** for interaction.

---


