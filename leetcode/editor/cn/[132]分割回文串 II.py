# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。 
# 
#  返回符合要求的 最少分割次数 。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2000 
#  s 仅由小写英文字母组成 
#  
#  
#  
#  Related Topics 动态规划 
#  👍 312 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0

        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        dp = [len(s) for i in range(len(s))]
        for i in range(0, len(s)):
            self.centeralExtend(s, i, i, dp)
            self.centeralExtend(s, i, i + 1, dp)
        return dp[-1]

    def centeralExtend(self, string, left, right, dp):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            if left > 0:
                dp[right] = min(dp[right], dp[left - 1] + 1)
            else:
                dp[right] = 0
            print(dp)
            left -= 1
            right += 1

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minCut('aaasdasdasdd'))