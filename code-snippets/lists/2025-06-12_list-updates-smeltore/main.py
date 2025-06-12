def smelt_ore(inventory):
    if inventory[1] == "Iron Ore": # Checks 2nd inventory slot for Iron Ore
        inventory[1] = "Iron Bar" # Chages it to Iron Bar
    return inventory
