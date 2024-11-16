class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 중복 제거 및 빠른 검색을 위해 set으로 변환
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # num이 시퀀스의 시작점인 경우에만 처리
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 연속된 숫자를 찾으며 streak 증가
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # 가장 긴 streak 업데이트
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
