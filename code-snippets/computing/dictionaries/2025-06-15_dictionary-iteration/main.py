def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf") # Sets counter to minus infinity
    most_common_enemy = None # Sets most common enemy to None
    for name in enemies_dict: # The name variable gets assigned each key from the dictionary, one at a time as you loop through
        count = enemies_dict[name] # Using the name (key) to look up it's corresponding value (the count) from the dictionary
        if count > max_so_far: # Checks if count value is higher than max_so_far value we set
            max_so_far = count # Updates max_so_far with highest count 
            most_common_enemy = name # Updates most_common_enemy with corresponding name (key) 
    return most_common_enemy # Returns most common enemy 

