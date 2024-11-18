class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 마지막에 while을 탈출할 때 left와 right가 범위를 벗어났으므로 [left+1:right]를 반환
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # 홀수 길이 회문
            palindrome1 = expandAroundCenter(i, i)
            # 짝수 길이 회문
            palindrome2 = expandAroundCenter(i, i + 1)

            # 가장 긴 회문 갱신
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest
