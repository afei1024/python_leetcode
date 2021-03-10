# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "1 + 1"
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 2-1 + 2 "
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 105 
#  s 由数字、'+'、'-'、'('、')'、和 ' ' 组成 
#  s 表示一个有效的表达式 
#  
#  Related Topics 栈 数学 
#  👍 397 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in {"+", "-"}:
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res
# leetcode submit region end(Prohibit modification and deletion)
