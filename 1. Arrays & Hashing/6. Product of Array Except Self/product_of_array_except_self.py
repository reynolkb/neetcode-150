from typing import List


class Solution(object):
    # nums = [1, 2, 3, 4]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1, 1, 1, 1]
        res = [1] * (len(nums))
        """
        the first loop is the product of everything to the left of the current num
        the second loop is the product of everything to the right of the current num
        for the second loop, postfix holds the product of everything, since you need to multiply that by the res[i]
        """

        """
        i = 1: res[1] = res[0] * nums[0] = 1 * 1 = 1, so res = [1, 1, 1, 1]
        i = 2: res[2] = res[1] * nums[1] = 1 * 2 = 2, so res = [1, 1, 2, 1]
        i = 3: res[3] = res[2] * nums[2] = 2 * 3 = 6, so res = [1, 1, 2, 6]
        """
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        """
        res = [1, 1, 2, 6]

        i = 3:
        postfix = 1
        res[3] *= postfix = 6 * 1 = 6
        postfix *= nums[3] = 1 * 4 = 4
        res=[1,1,2,6]

        i = 2:
        postfix = 4
        res[2] *= postfix = 2 * 4 = 8
        postfix *= nums[2] = 4 * 3 = 12
        res=[1,1,8,6]

        i = 1:
        postfix = 12
        res[1] *= postfix = 1 * 12 = 12
        postfix *= nums[1] = 12 * 2 = 24
        res=[1,12,8,6]

        i = 0:
        postfix = 24
        res[0] *= postfix = 1 * 24 = 24
        postfix *= nums[0] = 24 * 1 = 24
        res=[24,12,8,6]
        """
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
