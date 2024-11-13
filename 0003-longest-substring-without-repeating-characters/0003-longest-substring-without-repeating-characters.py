class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        max_len = 0
        for i in range(len(s)):
            if s[i] not in arr:
                arr.append(s[i])
            else:
                max_len = max(max_len, len(arr))
                arr = arr[arr.index(s[i]) + 1:]
                arr.append(s[i])
        max_len = max(max_len, len(arr))
        return max_len
