class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.globalCombinations = []
        self.backtrack(0, [], nums, target)
        return self.globalCombinations
    
    def backtrack(self, index: int, curr: List[int], nums: List[int], target: int) -> None:
        currSum = sum(curr)
        if currSum == target:
            self.globalCombinations.append(curr[:])
            return

        if index == len(nums) or currSum > target:
            return
        
        curr.append(nums[index])
        self.backtrack(index, curr, nums, target)
        curr.pop()
        self.backtrack(index + 1, curr, nums, target)



'''
Combination Sum
Solved 
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: 
nums = [2,5,6,9] 
target = 9

Output: [[2,2,5],[9]]
'''