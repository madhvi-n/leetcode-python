class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
#         n1 = len(nums1)
#         n2 = len(nums2)
        
#         dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

#         for i in range(1, n1 + 1):
#             for j in range(1, n2 + 1):
#                 if nums1[i - 1] == nums2[j - 1]:
#                     dp[i][j] = 1 + dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

#         return dp[n1][n2]

        dp = [[0 for j in range(len(nums2) + 1)] for i in range(len(nums1) + 1)]

        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]