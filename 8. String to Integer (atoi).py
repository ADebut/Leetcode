class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = ''
        flag = 0
        integer = ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if str == '' or str == '+' or str == '-' or str == " ":
            return 0
        for i in str:
            if i == '.' and flag == 1:
                break
            if i not in integer:
                if flag == 0:
                    if i == ' ':
                        continue
                    else:
                        return 0
                elif flag == 1:
                    if i == ' ':
                        break
                    else:
                        break
            if i in integer:
                if flag == 1 and (i == '+' or i == '-'):
                    break
                flag = 1
                s += i

        if s == '':
            return 0
        try:
            s = int(s)
        except:
            return 0
        s = int(s)
        if s < -2**31:
            return -2**31
        elif s > 2**31 - 1:
            return 2**31 - 1
        return s
            