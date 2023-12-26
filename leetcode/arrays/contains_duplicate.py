def containsDuplicate(nums) -> bool:
    return len(nums) != len(set(nums))

# Accepts a list as parameter. Returns a bool value. Sets don't allow duplication.
# Comparing the lengths will reveal if a duplicate element existed
