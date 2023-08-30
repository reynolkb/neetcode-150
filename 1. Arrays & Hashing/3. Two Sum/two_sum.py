from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}

        for numIndex, num in enumerate(nums):
            possibleMatch = target - num
            if possibleMatch in numDict:
                return [numDict[possibleMatch], numIndex]
            numDict[num] = numIndex


def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Two Sum:", result)


if __name__ == "__main__":
    main()
