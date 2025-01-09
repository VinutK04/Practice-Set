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

# 2nd Question
def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
    return stack == []

givenStr = "()[]{"
print(isValid(givenStr))

# 3rd Question
def topKFrequent(nums, k):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_count[:k]]
    
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
