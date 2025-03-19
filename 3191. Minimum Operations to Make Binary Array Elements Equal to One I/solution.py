# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_operations = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                n_operations += 1
                nums[i] = 1
                nums[i + 1] = nums[i + 1] ^ 1
                nums[i + 2] = nums[i + 2] ^ 1

        return -1 if nums[i + 1] + nums[i + 2] != 2 else n_operations
