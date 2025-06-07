class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.globalCombinations = []
        candidates.sort()
        self.backtrack(0, [], candidates, target)
        return self.globalCombinations
    
    def backtrack(self, index: int, curr: List[int], candidates: List[int], target: int):
        currSum = sum(curr)
        if currSum == target:
            if curr not in self.globalCombinations:
                self.globalCombinations.append(curr[:])
            return
        
        if index == len(candidates) or currSum > target:
            return
        
        curr.append(candidates[index])
        self.backtrack(index + 1, curr, candidates, target)
        curr.pop()

        while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
            index += 1

        self.backtrack(index + 1, curr, candidates, target)
        

'''
Combination Sum II
Solved 
You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
Example 2:

Input: candidates = [1,2,3,4,5], target = 7

Output: [
  [1,2,4],
  [2,5],
  [3,4]
]
'''