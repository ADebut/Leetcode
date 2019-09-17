class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        s = list(s)
        print(s)
        while(i < j):
            if s[i] in vowel and s[j] in vowel:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            elif s[i] in vowel and s[j] not in vowel:
                j -= 1
            elif s[i] not in vowel and s[j] in vowel:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s)