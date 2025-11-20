'''
@index 15
@title 三数之和
@difficulty 中等
@tags array,two-pointers,sorting
@draft false
@link https://leetcode.cn/problems/3sum/description/
@frontendId 15
@solved false
'''
from typing import List  # 导入类型注解模块，用于类型提示

class Solution:  # 定义解决方案类
    def threeSum(self,nums: List[int]) -> List[List[int]]:  # 三数之和方法，接收整数数组，返回所有不重复的三元组
        ans = []  # 初始化结果列表，用于存储所有满足条件的三元组
        nums.sort()  # 对数组进行排序，便于使用双指针和去重
        n = len(nums)  # 获取数组长度
        
        for i in range(n-2):  # 遍历数组，固定第一个数，至少需要3个数所以到n-2
            x = nums[i]  # 获取当前固定的第一个数
            if i > 0 and x == nums[i-1]:  # 跳过重复的第一个数，避免重复的三元组
                continue  # 如果当前数与上一个数相同，跳过本次循环
            j = i + 1  # 左指针初始化为第一个数之后的位置
            k = n - 1  # 右指针初始化为数组最后一个位置
            s = x + nums[j] + nums[k]  # 计算当前三个数的和（初始值，后续会在循环中更新）

            if x + nums[-1] + nums[-2] < 0:  # 剪枝：如果当前固定的数加上最大的两个数仍小于0，说明后续所有组合都小于0
                break  # 直接跳出循环，因为数组已排序，后续组合只会更小
                
            
            
            while j < k:  # 当左右指针未相遇时继续循环
                if s > 0:  # 如果三数之和大于0
                    k -= 1  # 右指针左移，减小和的值（因为数组已排序）
                    s = x + nums[j] + nums[k]  # 更新三数之和
                elif s < 0:  # 如果三数之和小于0
                    j += 1  # 左指针右移，增大和的值（因为数组已排序）
                    s = x + nums[j] + nums[k]  # 更新三数之和
                else:  # 如果三数之和等于0，找到一组答案
                    ans.append([x,nums[j],nums[k]])  # 将当前三元组添加到结果列表
                    j += 1  # 左指针右移，继续寻找下一个可能的组合
                    if j < k and nums[j] == nums[j-1]:  # 跳过重复的左指针值，避免重复的三元组
                        j += 1  # 如果当前值与上一个值相同，继续右移
                    k -= 1  # 右指针左移，继续寻找下一个可能的组合
                    if k > j and nums[k] == nums[k+1]:  # 跳过重复的右指针值，避免重复的三元组
                        k -= 1  # 如果当前值与下一个值相同，继续左移
                        
        return ans  # 返回所有满足条件的三元组列表
                    
