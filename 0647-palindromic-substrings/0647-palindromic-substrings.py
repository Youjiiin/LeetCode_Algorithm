class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def isPal(string):
            return string == string[::-1]

        answer = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if isPal(substring):
                    answer += 1
        return answer
