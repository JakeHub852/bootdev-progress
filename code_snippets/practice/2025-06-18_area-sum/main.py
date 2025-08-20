def area_sum(rectangles):
    area = 0
    for rect in rectangles:
        height = rect["height"]
        width = rect["width"]
        area += height * width
    return area

def area_sum(rectangles):
    # Initialize a variable 'area' to keep track of the total sum.
    # We start at 0 because no area has been added yet.
    area = 0

    # Iterate through each 'rect' (rectangle dictionary) in the input list 'rectangles'.
    # This loop will run once for every rectangle in the list.
    for rect in rectangles:
        # Inside the loop, access the value associated with the key "height"
        # from the current rectangle dictionary and store it in 'height'.
        height = rect["height"]

        # Access the value associated with the key "width"
        # from the current rectangle dictionary and store it in 'width'.
        width = rect["width"]

        # Calculate the area of the current rectangle (height * width)
        # and add it to the running total stored in the 'area' variable.
        area += height * width

    # After the loop has finished processing all rectangles,
    # return the final accumulated area sum.
    return area