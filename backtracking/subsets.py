class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.globalNums = []
        self.backtrack(0, [], nums)
        return self.globalNums
    
    def backtrack(self, index: int, curr: List[int], nums: List[int]) -> None:
        if index == len(nums):
            self.globalNums.append(curr[:])
            return

        curr.append(nums[index])
        self.backtrack(index + 1, curr, nums)
        curr.pop()
        self.backtrack(index + 1, curr, nums)


'''
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
'''