'''
@index 167
@title 两数之和 II - 输入有序数组
@difficulty 中等
@tags array,two-pointers,binary-search
@draft false
@link https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
@frontendId 167
@solved false
'''
from typing import List  # 导入类型注解模块，用于类型提示
class solution:  # 定义解决方案类
    def twoSum(self,numbers:List[int],target:int) -> List[int]:  # 双指针方法，接收有序数组和目标值，返回两个索引（从1开始）
        left = 0  # 左指针初始化为数组第一个元素的下标
        right = len(numbers)-1  # 右指针初始化为数组最后一个元素的下标
        
        while left < right:  # 当左右指针未相遇时继续循环
            x = numbers[left] + numbers[right]  # 计算当前左右指针指向的两个元素之和
            if x == target:  # 如果和等于目标值
                break  # 找到答案，跳出循环
            if x < target:  # 如果和小于目标值
                left += 1  # 左指针右移，增大和的值（因为数组有序）
            else:  # 如果和大于目标值
                right -= 1  # 右指针左移，减小和的值（因为数组有序）
                
        return [left+1,right+1]  # 返回两个索引（题目要求从1开始计数，所以加1）    
            
            

