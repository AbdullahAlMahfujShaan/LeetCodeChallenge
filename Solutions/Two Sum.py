class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store the number and its index
        num_dict = {}
        # Iterate over the list to check each element
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []