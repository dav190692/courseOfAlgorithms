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


#________________________________________________________________
# leetcode 121
# best time to buy and sell stock

# def max_profit(prices):
#     buy, sell = 0, 1
#     max_profit = 0

#     while sell < len(prices):
#         if prices[buy] < prices[sell]:
#             profit = prices[sell] - prices[buy]
#             max_profit = max(max_profit, profit)
#         else:
#             buy = sell
#         sell += 1
#     return max_profit



# prices = [1, 2, 3, 8]


# print(max_profit(prices))

#________________________________________________________________




#________________________________________________________________
#leetcode 217
# contains duplicate
# def containsDuplicate(nums):
#     hashset = set()

#     for  i in  nums:
#         if i in hashset:
#             return True
#         hashset.add(i)
#     return False


# nums = [1, 2, 3, 8, 1]


# print(containsDuplicate(nums))



#________________________________________________________________



#________________________________________________________________
# leetcode 238
# product of Array except self
# def product(arr):
#     res = [1] * len(arr)
#     prefix = 1

#     for i in range(len(arr)):
#         res[i] = prefix
#         prefix *= arr[i]


#     postfix = 1

#     for i in range(len(arr) - 1, -1, -1):
#         res[i] *= postfix
#         postfix *= arr[i]

#     return res



# arr = [3, 8, 9]


# print(product(arr))

#________________________________________________________________



#________________________________________________________________
# leetcode 53
# max subarraay

# def mmaxSubArray(arr):
#     maxSub = arr[0]
#     cursum = 0
#     for n in arr:
#         if cursum < 0:
#             cursum = 0
#         cursum += n
#         maxSub = max(maxSub, cursum)

#     return maxSub



# arr = [1, 2, 3, -1, -2, -5, 7, 8]


# print(mmaxSubArray(arr))


#________________________________________________________________



#________________________________________________________________
# leetcode 152
# MaximumProductSubarray

# def maxProduct(nums):
#     res = max(nums)

#     curMin, curMax = 1, 1

#     for n in nums:
#         if n == 0:
#             curMin, curMax = 1, 1
#             continue
#         tmp = curMax * n
#         curMax = max(n * curMax, n * curMin, n)
#         curMin = min(tmp, n * curMin, n)
#         res = max(res, curMax, curMin)

#     return res


# arr = [-1, -2, -4]


# print(maxProduct(arr))

#________________________________________________________________



#________________________________________________________________
# leetcode 153
# Find minimum in Rotated sorted array


# def findMin(arr):
#     res = arr[0]

#     l, r = 0, len(arr) -1

#     while l <= r:
#         if arr[l] < arr[r]:
#             res = min(res, arr[l])
#             break
#         m = (l +r) // 2
#         res = min(res, arr[m])

#         if arr[m] >= arr[l]:
#             l = m + 1
#         else:
#             r = m -1
#     return res



# arr = [ 7, 8, 1, 2, 3, 4, 5, 6,]

# print(findMin(arr))

#________________________________________________________________




#________________________________________________________________
# leetcode 33
# search in rotate sorted array


# def search(nums, target):
#     l,r = 0, len(nums) -1

#     while l <= r:
#         mid = (l + r) // 2
#         if nums[mid] == target:
#             return mid
        
#         if nums[l] <= nums[mid]:
#             if target > nums[mid] or target < nums[l]:
#                 l = mid + 1
#             else:
#                 r = mid -1
#         else:
#             if target < nums[mid] or target > nums[r]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
    
            
#     return -1




# target = 6

# arr = [ 4, 5, 6, 7, 8, 1, 2, 3]


# print(search(arr, target))


#________________________________________________________________



#________________________________________________________________
# leetcode 15
# 3 sum

# def threeSum(nums):
#     res = []
#     nums.sort()


#     for i, a in enumerate(nums):
#         if i > 0 and a == nums[i -1]:
#             continue
#         l, r = i+ 1, len(nums) -1

#         while l < r:
#             threeSum = a + nums[l] + nums[r]
#             if threeSum > 0:
#                 r -= 1
#             elif threeSum < 0:
#                 l += 1
#             else:
#                 res.append([a, nums[l], nums[r]])
#                 l += 1
#                 while nums[l] == nums[l-1] and l < r:
#                     l += 1
    
#     return res



# nums = [0,0,0]


# print(threeSum(nums))

#________________________________________________________________


#________________________________________________________________
# leetcode 11
# Container with most water



# brute force
# def maxArea(heigth):
#     res = 0
#     for l in range(len(heigth)):
#         for r in range(l + 1, len(heigth)):
#             area = (r - l) * min(heigth[r], heigth[l])
#             res = max(res, area)
#     return res


#liner time solutiuon


# def maxArea(heigth):
#     res = 0
#     l, r = 0, len(heigth) - 1

#     while l < r:
#         area = (r - l) * min(heigth[r], heigth[l])
#         res  = max(res, area)


#         if heigth[l] < heigth[r]:
#             l += 1
#         else:
#             r -= 1

#     return res


#________________________________________________________________





#________________________________________________________________
# leetcode 371
# Sum of Two Integers

# def sumOfTwoInt(a, b):
#     while( b != 0):
#         temp =  (a & b) << 1
#         a = a ^ b
#         b = temp
#     return a


# print(sumOfTwoInt(12, 89))

#________________________________________________________________



#________________________________________________________________
# leetcode 191
# number of one bits

# def hammingWeight(n):
#     res = 0
#     while n:
#         res +=  n % 2
#         n = n >> 1
#     return res





# def hammingWeight(n):
#     res = 0
#     while n:
#         n = n & (n -1)
#         res +=  1
        
#     return res


# print(hammingWeight(101))



#________________________________________________________________




#________________________________________________________________
# leetcode 338
# Counting bits



# def countBits(n):
#     dp = [0] * (n + 1)
#     offset = 1



#     for i in range(1, n + 1):
#         if offset * 2 == i:
#             offset = i
#         dp[i] = 1 + dp[i - offset]

#     return dp


# print(countBits(1))

#________________________________________________________________




#________________________________________________________________
# leetcode 268
# Missing Number



# def missingNumber(nums):
#     res = len(nums)


#     for i in range(len(nums)):
#         res += (i - nums[i])

#     return res
    



#________________________________________________________________

#________________________________________________________________
# leeetcode 190
# reverse bits


# def reverseBits(n):
#     res  = 0

#     for i in range(32):
#         bit = (n >> i) & 1
#         res =  res | (bit << (31 - i))

#     return res


# print(reverseBits(10))

#________________________________________________________________



#________________________________________________________________
# leetcode 70
# climbing Stairs


# def climbstairs(n):
#     one, two = 1, 1

#     for i in range(n -1):
#         temp  = one
#         one = one + two
#         two  = temp
#     return one




#________________________________________________________________


#________________________________________________________________
# leetcode 322
# Coin Change


# def coinChange(coins, amount):
#     dp = [amount + 1] * (amount + 1)
#     dp[0] = 0


#     for a in range(1, amount + 1):
#         for c in coins:
#             if a - c >= 0:
#                 dp[a] =  min(dp[a], 1 + dp[a - c])


#     return dp[amount] if dp[amount] != amount + 1 else -1


# coins = [1, 2, 3, 4]
# amount = 5

# print(coinChange(coins, amount))


#________________________________________________________________



#________________________________________________________________
# leetcode 300
# Longest Incresing subsequence
# def lengthOfLIS(nums):
#     LIS = [1] * len(nums)


#     for i in range(len(nums) - 1, -1, -1):
#         for j in range(i+1, len(nums)):
#             if nums[i] < nums[j]:
#                 LIS[i] = max(LIS[1], 1 + LIS[j])


#     return max(LIS)



# ls = [1, 2, 3, 5, 4, 5, 6]

# print(lengthOfLIS(ls))



#________________________________________________________________



#________________________________________________________________
# leetcode 1143
# Longest common Subsequence

# def longestCommonSubsequence(text1, text2):
#     dp = [[0 for j in range(len(text2 + 1))] for i in range(len(text1) + 1)]

#     for i in range(len(text1) -1, -1, -1):
#         for j in range(len(text2) -1, -1, -1):
#             if text1[i] == text2[j]:
#                 dp[i][j] = 1 + dp[i + 1][j + 1]
#             else:
#                 dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])



#     return dp[0][0]


#________________________________________________________________


#________________________________________________________________
# leetcode 139
# woed break


# def wordBreak(s, wordDict):
#     dp = [False] * (len(s) + 1)
#     dp[len(s)] = True

#     for i in range(len(s) - 1, -1, -1):
#         for w in wordDict:
#             if i + len(w) <= len(s) and s[i:i + len(w)] == w:
#                 dp[i] = dp[i + len(w)]
#             if dp[i]:
#                 break


#     return dp[0]



# s = 'leetcode'

# wodDict = ['leet', 'code', 'ddd']


# print(wordBreak(s, wodDict))

#________________________________________________________________



#________________________________________________________________
# leetcode 39
# combination Sum


# def combinationSum(candidates, target):
#     res = []
#     def dfs(i, cur, total):
#         if total == target:
#             res.append(cur.copy())
#             return
#         if i >= len(candidates) or total > target:
#             return
        
#         cur.append(candidates[i])
#         dfs(i, cur, total + candidates[i])
#         cur.pop()
#         dfs(i + 1, cur, total)
        

#     dfs(0, [], 0)

#     return res

#________________________________________________________________
#________________________________________________________________
# leetcode 198
# house robber I

# def rob(nums):
#     rob1, rob2 = 0, 0

#     for n in nums:
#         temp = max(n + rob1, rob2)
#         rob1 = rob2
#         rob2 = temp

#     return rob2


# ls = [1, 2, 3, 1]

# print(rob(ls))


#________________________________________________________________

#________________________________________________________________
# leetcode 198
# house robber II





# def helper(nums):
#     rob1, rob2 = 0, 0

#     for n in nums:
#         temp = max(n + rob1, rob2)
#         rob1 = rob2
#         rob2 = temp

#     return rob2


# def rob(nums):
#     return max(nums[0], helper(nums[1:]), helper(nums[:-1]))



# ls = [2, 3, 6, 2]

# print(rob(ls))
#________________________________________________________________


#________________________________________________________________
# leetcode  91
# decode ways


# def numDecodings(s: str):
#     dp = {len(s) : 1}

#     def dfs(i):
#         if i in dp:
#             return dp[i]
#         if s[i] == '0':
#             return 0
#         res  = dfs(i + 1)
#         if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456')):
#             res += dfs(i + 2)
#         dp[i] = res
#         return res
#     return dfs(0)



# s  = '129'


# print(numDecodings(s))

    
#________________________________________________________________


#________________________________________________________________
# leetcode 62
# unique paaths


# def uniquePaths(m, n):
#     row = [1] * n

#     for i in range(m -1):
#         newRow = [1] * n
#         for j in range(n-2, -1, -1):
#             newRow[j] = newRow[j + 1] + row[j]
#         row = newRow
#     return row[0]


#________________________________________________________________



#________________________________________________________________
# leetcode 55
# Jump game


# def canJump(nums):
#     goal = len(nums) - 1

#     for i in range(len(nums) -1, -1, -1):
#         if i + nums[i] >= goal:
#             goal = i

#     return True if goal == 0 else False





#________________________________________________________________



#________________________________________________________________
# leetcode 133
# clone
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# class Solution:
#     def cloneGraph(self, node: 'Node'):
#         oldToNew = {}

#         def dfs(node):
#             if node in oldToNew:
#                 return oldToNew[node]
            

#             copy = Node(node.val)
#             oldToNew[node] = copy

#             for nei in node.neighbors:
#                 copy.neighbors.append(dfs(nei))
            

#             return copy
        
#         return dfs(node) if node else None
            



#________________________________________________________________



#________________________________________________________________
# leetcode 207
# course Schedule


# def canFinish(numCourses, prerequisites):
#     preMap = {i : [] for i in range(numCourses)}

#     for crs, pre in prerequisites:
#         preMap[crs].append(pre)

#     visetSet = set()


#     def dfs(crs):
#         if crs in visetSet:
#             return False
#         if preMap[crs] == []:
#             return True
        

#         visetSet.add(crs)

#         for pre in preMap[crs]:
#             if not dfs(pre): return False
        

#         visetSet.remove(crs)
#         preMap[crs] = []
#         return True
    
#     for crs in range(numCourses):
#         if not dfs(crs): return False
#     return True

#________________________________________________________________


#________________________________________________________________
# leetcode 417
# pacific atlantic water flow

# def pacificAtlantic(heights):
#     ROWS, COLS = len(heights), len(heights[0])
#     pac, atl = set(), set()



#     for c in range(COLS):




# kisata


#________________________________________________________________




#________________________________________________________________
# leetcode 200
# Number of Islands
# from collections import deque

# class Solution:
#     def numIslands(grid):
#         if not grid:
#             return 0
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         islands = 0

#         def bfs(r, c):
#             q = deque()
#             visit.add((r, c))
#             q.append((r, c))

#             while q:
#                 row, col = q.popleft()
#                 directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#                 for dr, dc in directions:
#                     r, c  = row + dr, col + dc
#                     if (r in range(rows) and
#                         c in range(cols) and
#                         grid[r][c] == '1' and
#                         (r, c) not in visit):
                        
#                         q.append((r, c))
#                         visit.add((r, c))


#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1' and (r, c) not in visit:
#                     bfs(r, c)
#                     islands += 1
#         return islands




#________________________________________________________________

#________________________________________________________________
# leetcode 128
# longest consecutive sequence


def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest



#________________________________________________________________




#________________________________________________________________
# leetcode 269
# topological sort

# def alienOrder(words):
#     adj = {c: set() for w in words for c in w }


#     for i in range(len(words)-1):
#         w1, w2 = words[i], words[i + 1]
#         minLen= min(len(w1), len(w2))
#         if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
#             return ""
#         for j in range(minLen):
#             if w1[j] != w2[j]:
#                 adj[w1[j]].add(w2[j])
#                 break

#     visit = {}
#     res = []

#     def dfs(c):
#         if c in visit:
#             return visit[c]
            
#         visit[c] = True

#         for nei in adj[c]:
#             if dfs(nei):
#                 return True
#         visit[c] = False

#         res.append(c)
        
#     for c in adj:
#         if dfs(c):
#             return ""
            
#     res.reverse()
#     return "".join(res)
            


# words = ['wrt', 'wrf', 'er', 'ett', 'rftt']

# print(alienOrder(words))

#________________________________________________________________


#________________________________________________________________
# leetcode 178
# graph valid tree



# def validTree(n, edges):
#     if not n:
#         return True
    

#     adj = {i : [] for i in range(n)}

#     for n1, n2 in edges:
#         adj[n1].append(n2)
#         adj[n2].append(n1)

#     visit = set()
#     def dfs(i, prev):
#         if i in visit:
#             return False
        
#         visit.add(i)

#         for j in adj[i]:
#             if j == prev:
#                 continue
#             if not dfs(j, i):
#                 return False
            
#         return True
    

#     return dfs(0, -1) and n == len(visit)


#________________________________________________________________





#________________________________________________________________
# leetcode 323
# Number of Connected Components in an Undirected Graph


# union algorithm

# def countComponents(n, edges):
#     par = [i for i in range(n)]
#     rank = [1] * n

#     def find(n1):
#         res = n1

#         while res != par[res]:
#             par[res] = par[par[res]]
#             res = par[res]
#         return res
    
#     def union(n1, n2):
#         p1, p2 = find(n1), find(n2)

#         if p1 == p2:
#             return 0
#         if rank[p2] > rank[p1]:
#             par[p1] = p2
#             rank[p2] += rank[p1]
#         else:
#             par[p2] =p2
#             rank[p1] += rank[p2]
#         return 1
    

#     res = n
#     for n1, n2 in edges:
#         res -= union(n1, n2)


#     return res








#________________________________________________________________


#________________________________________________________________
# leetcode 206
# reverse Linked List


# def reverseList(head):
#     prev, curr = None, head
#     while curr:
#         after = curr.next
#         curr.next = prev
#         prev = curr
#         curr = after
#     return prev

# def recursive(head):
#     if not head:
#         return None

#     new_head = head

#     if head.next:
#         new_head = recursive(head.next)
#         head.next.next = head

#     head.next = None
#     return new_head

#________________________________________________________________



#________________________________________________________________
# leetcode 141
# Linked LIst Cycle


# def hasCycle(head):
#     slow, fast = head, head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True
#     return False
        




#________________________________________________________________



#________________________________________________________________
# leetcode 21 
# merge two sorted list
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummy = ListNode()
#         tail  = dummy

#         while l1 and l2:
#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next

#         if l1:
#             tail.next = l1
#         elif  l2:
#             tail.next = l2


#         return dummy.next



#________________________________________________________________


from collections import deque


st = deque()
 












































        

