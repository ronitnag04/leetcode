class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        while '' not in strs:
            if all([strs[0][0] == strs[i][0] for i in range(1, len(strs))]):
                prefix += strs[0][0]
                for i in range(len(strs)):
                    strs[i] = strs[i][1:]
            else:
                return prefix
        return prefix
        