from typing import List

def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    result = []

    # Step 1: Find the maximum number of candies any kid currently has
    max_candies = max(candies)

    # Step 2: For each kid, check if giving them all extraCandies makes their total >= maxCandies
    for candy in candies:
        result.append(candy + extra_candies >= max_candies)

    return result

# Driver code for testing
print(kids_with_candies([2, 3, 5, 1, 3], 3)) # Output: {True, True, True, False, True}
print(kids_with_candies([4, 2, 1, 1, 1,2], 1)) # Output: {True, False, False, False, False}
print(kids_with_candies([12, 1, 12], 10)) # Output: {True, False, True}