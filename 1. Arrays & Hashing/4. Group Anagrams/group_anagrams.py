import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            # Initialize a list of 26 zeros to represent each letter of the alphabet
            count = [0] * 26
            for c in s:
                # Subtract the ASCII value of 'a' from the ASCII value of 'c' to get the position of 'c' in the alphabet
                # Increment the count for that position to keep track of the number of times that letter has occurred in the string
                count[ord(c) - ord("a")] += 1
            # Convert the count list to a tuple to use as a key in the dictionary
            # 'eat' would be represented as (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
            # Use this tuple key to append the string 's' to the list in the dictionary
            # by conversting the count list to a tuple, it becomes immutable and can be used as a key
            ans[tuple(count)].append(s)
        return ans.values()


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result = solution.groupAnagrams(strs)
    print(list(result))


if __name__ == "__main__":
    main()
