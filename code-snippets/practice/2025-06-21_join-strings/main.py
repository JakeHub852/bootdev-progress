def join_strings(strings):
    mystring = "" # Initialize empty string
    for string in strings: # Loops through every string in the list 
       mystring += (string + ",") # Add to mystring concatenated with a comma 
    return mystring[:-1] # Use slicing to remove final comma
    
        