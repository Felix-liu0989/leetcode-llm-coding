'''  # 元信息注释块开头
@index 20  # 题目编号
@title 有效的括号  # 题目标题
@difficulty 简单  # 难度级别
@tags stack,string  # 使用到的标签
@draft false  # 是否草稿
@link https://leetcode.cn/problems/valid-parentheses/description/  # 原题链接
@frontendId 20  # 前端展示编号
@solved false  # 是否已解决
'''  # 元信息注释块结尾

class Solution:  # 定义解题类
    def isValid(self,str:str) -> bool:  # 主方法，判断括号串是否有效
        left = []  # 用列表模拟栈保存尚未匹配的左括号
        for c in str:  # 遍历字符串中的每个字符
            if c in '({[':  # 如果遇到左括号
                left.append(c)  # 入栈保存
            else:  # 遇到右括号
                if left and self.leftof(c) == left[-1]:  # 栈不空且与栈顶匹配
                    left.pop()  # 弹出已匹配的左括号
                else:  # 否则匹配失败
                    return False  # 立即返回无效 函数会立即结束运行，不再继续遍历后续字符，直接把 False 返回给调用者，表示已经确认字符串无效
        return not left  # 所有字符处理完后栈为空则有效
    
    def leftof(self,c:str) -> str:  # 返回对应右括号的左括号
        if c == '}':  # 如果是右花括号
            return '{'  # 返回左花括号
        if c == ')':  # 如果是右圆括号
            return '('  # 返回左圆括号
        return '['  # 剩余情况只能是右方括号，返回左方括号


'''
例如输入字符串 `"({[]("`，
遍历过程如下：遇到 `'('`、`'{'`、`'['`、`']'` 都能成功匹配，
栈会依次 Push `'('`→`'{'`→`'['`，在遇到 `']'` 时
因匹配到 `'['` 被 Pop，
因此遍历到倒数第二个字符时栈里只剩下 `'('` 和 `'{'`。
最后一个字符还是 `'('`，它是左括号，没有与之对应的右括号出现，
因而整趟循环都没触发 `return False`，
但循环结束后 `left` 仍然是 `['(', '{', '(']`。
此时执行 `return not left` 得到 `False`，说明虽然右括号都匹配成功，
但仍有左括号滞留栈中，整体依旧是无效字符串。
'''