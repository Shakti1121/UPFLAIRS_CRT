
# 4. Function to find the max sum of k consecutive elements
def max_consecutive_sum(nums, k):
    return max(sum(nums[i:i + k]) for i in range(len(nums) - k + 1))

nums = [2, 3, 5, 1, 6, 2, 7, 4]
k = 3
print(max_consecutive_sum(nums, k))  # Output: Maximum sum of k consecutive elements
