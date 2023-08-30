from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()
        for num in nums:
            if num in duplicateSet:
                return True
            duplicateSet.add(num)
        return False


def main():
    nums = [1, 2, 3, 4, 2, 5]
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print("Contains duplicates:", result)


if __name__ == "__main__":
    main()
