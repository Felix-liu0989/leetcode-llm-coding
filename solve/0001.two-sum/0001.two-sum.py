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

from typing import List  # 导入类型注解模块，用于类型提示

class Solution:  # 定义解决方案类
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # 两数之和方法，接收整数数组和目标值，返回两个数的索引
        idx = {}  # 创建哈希表（字典），用于存储已遍历过的数字及其索引，键为数字值，值为索引
        
        for j, x in enumerate(nums):  # 遍历数组，j为当前索引，x为当前元素值
            left = target - x  # 计算需要的另一个数（目标值减去当前数）
            if left in idx:  # 如果需要的数已经在哈希表中（说明之前遍历过）
                return [idx[left], j]  # 返回之前存储的索引和当前索引，找到答案
            
            idx[x] = j  # 将当前数字和索引存入哈希表，供后续查找使用




