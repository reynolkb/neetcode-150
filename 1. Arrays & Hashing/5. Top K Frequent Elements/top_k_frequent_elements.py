from typing import List


class Solution:
    # nums = [1,1,1,2,2,3]
    # k = 2
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # key = number, value = count
        # count = {1:3, 2:2, 3:1}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # freq = [[], [3], [2], [1], [], []]
        # 3 occured once, 2 occured twice, 1 occured three times
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # start at last index, stop at 1, step by -1
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print("Top K Frequent Elements:", result)


if __name__ == "__main__":
    main()
