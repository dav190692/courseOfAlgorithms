#217. Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/description/

# class Solution(object):
#     def containsDuplicate(self, nums):


#         if len(nums) > len(set(nums)):
#             return True
#         return False
#________________________________________________________________
#169. Majority Element
#https://leetcode.com/problems/majority-element/

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = 0
#         candidate = 0
        
#         for num in nums:
#             if count == 0:
#                 candidate = num
            
#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1
        
#         return candidate
#________________________________________________________________
# 268. Missing Number
# https://leetcode.com/problems/missing-number/description/


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
        
#         # Case 1
#         if nums[0] != 0:
#             return 0
        
#         # Case 2
#         if nums[-1] != n:
#             return n
        
#         # Case 3
#         for i in range(1, len(nums)):
#             if nums[i] != i:
#                 return i
        
#         return 0
#________________________________________________________________


#  349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/description/
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#        return set(nums1) & set(nums2) 

#________________________________________________________________

# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         i = m - 1
#         j = n - 1
#         k = m + n - 1

#         while i >= 0 and j >= 0:
#             if nums1[i] < nums2[j]:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             else:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             k -= 1

#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1
        
#         return nums1

#________________________________________________________________

#1636. Sort Array by Increasing Frequency
#https://leetcode.com/problems/sort-array-by-increasing-frequency/description/

# class Solution:
#     def frequencySort(self, nums: List[int]) -> List[int]:

#         store = defaultdict(int)

#         for i in nums:
#             store[i] += 1

#         result = []

#         store_sorted = sorted(store.items(), key=lambda item: [item[1], -1*item[0]])

#         for key, value in store_sorted:

#             result = result + [key]*value

#         return result

#________________________________________________________________

#1. Two Sum
#https://leetcode.com/problems/two-sum/description/


# ls = [1,2, 4, 5, 67]
# target = 72
# def two_sum(nums, target):
#     di = {}
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         if temp in di:
#             return [di[temp], i]
#         di[nums[i]] = i




# print(two_sum(ls, target))
#________________________________________________________________


#121. Best Time to Buy and Sell Stock
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         lowest = prices[0]
#         for price in prices:
#             if price < lowest:
#                 lowest = price
#             res = max(res, price - lowest)
#         return res

#________________________________________________________________


#53. Maximum Subarray
#https://leetcode.com/problems/maximum-subarray/description/
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:        
#         newNum = maxTotal = nums[0]        
        
#         for i in range(1, len(nums)):
#             newNum = max(nums[i], nums[i] + newNum)
#             maxTotal = max(newNum, maxTotal)

#         return maxTotal	
#________________________________________________________________
#977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# from typing import List

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         return sorted(map(lambda x: x**2, nums))
    

# ls = [-1, 3, 5, 8, 6]

# solution = Solution()
# print(solution.sortedSquares(ls))
#________________________________________________________________




        

