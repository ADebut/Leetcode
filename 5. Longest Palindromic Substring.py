class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # def reverse(s):
        #     str1 = ''
        #     for i in s:
        #         str1 = i + str1
        #     return str1
        # if len(s) == 1 or len(s) == 0:
        #     return s
        # l = ''
        # n = 0
        # flag = 0
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s)):
        #         if s[i] == s[j]:
        #             if s[i:j+1] == reverse(s[i:j+1]):
        #                 flag = 1
        #                 n = j - i + 1
        #         if len(l) < n:
        #             l = s[i:j+1]
        # if flag == 0:
        #     return s[0]
        # return l
        n = len(s)
        if n < 1:
            return s
        
        # initialization of DP
        dp_mat = [[1] * n, [0] * (n - 1)]
        for i in range(n-1):
            dp_mat[1][i] = int(s[i] == s[i+1])
        for step in range(2, n):
            ref_getter = step % 2
            other = (step + 1) % 2
            ref = dp_mat[ref_getter]
            curr_stat = []
            for i in range(n-step):
                curr_stat.append(int(ref[i+1] and (s[i] == s[i + step])))
            if any(curr_stat + dp_mat[other]) == False:
                break
            dp_mat[ref_getter] = curr_stat
        min_l = n+1
        ans_row = []
        for row in dp_mat:
            if any(row) and len(row) < min_l:
                ans_row = row
                min_l = len(row)

        idx = ans_row.index(1)
        leng = n - min_l + 1
        return s[idx:idx+leng]