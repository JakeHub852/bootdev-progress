def count_enemies(enemy_names):
    enemies_dict = {} # Initialize dictionary
    for enemy_name in enemy_names: # Loop through enemy names
        if enemy_name in enemies_dict: 
            enemies_dict[enemy_name] += 1 # If enemy is already a key in enemies dictionary, increment by 1. (Another sighting)
        else:
            enemies_dict[enemy_name] = 1 # If not add it to dictionary with value of 1. (First sighting)
    return enemies_dict
