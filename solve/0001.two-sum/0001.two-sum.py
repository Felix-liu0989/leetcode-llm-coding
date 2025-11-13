'''
@index 1
@title 两数之和
@difficulty 简单
@tags array,hash-table
@draft false
@link https://leetcode.cn/problems/two-sum/description/
@frontendId 1
@solved true
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        
        for j, x in enumerate(nums):
            left = target - x
            if left in idx:
                return [idx[left], j]
            
            idx[x] = j




