class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = [*nums1, *nums2]
        nums.sort()
        if len(nums)%2 == 0:
            a = nums[int(len(nums)/2)-1]
            a_1 = nums[int(len(nums)/2)]
            return (a+a_1)/2
        else:
            return nums[int(len(nums)/2)]
