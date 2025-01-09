# 1st Question
nums = [2, 4, 4, 7]
target = 11

res = []
seen = set()  # We can use a set instead of a dictionary for faster lookups

for idx, val in enumerate(nums):
    complement = target - val
    if complement in seen:  # Check if the complement is in the set
        res = [nums.index(complement), idx]  # Get the first index of complement and current index
        break
    seen.add(val)  # Add the current value to the set

print(res)
