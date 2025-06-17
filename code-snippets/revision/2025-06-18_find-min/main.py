def find_min(nums):
    smallest_number = float("inf")
    for number in nums:
        if number < smallest_number:
            smallest_number = number
    return smallest_number
