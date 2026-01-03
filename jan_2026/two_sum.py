#https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in nums:
            nums[nums.index(a)] = "InUse"
            for b in nums:
                if isinstance(b,int):
                    if a+b == target:
                        return [nums.index("InUse"),nums.index(b)]
            nums[nums.index("InUse")] = a

#Note:
#This was my first solved leetcode problem :)
