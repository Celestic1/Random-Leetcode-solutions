class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        d = {}
        substr = ''
        i = 0
        curr = 1
        while i < len(s):
            if s[i] not in substr:
                substr += s[i]
                i += 1
            else:
                d[substr] = len(substr)
                substr = ''
                i = curr
                curr += 1
        d[substr] = len(substr)
        return max(d.values())
