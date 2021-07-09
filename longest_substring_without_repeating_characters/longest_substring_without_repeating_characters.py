class Solution(object):
    # sliding window algorithm
    def lengthOfLongestSubstring(self,s):
        max_length = 0
        lista = []
        count = 0
        while count < int(len(s)):
            if s[count] not in lista:
                lista.append(s[count])
                max_length = max(max_length, len(lista))
                count += 1
            else:
                lista.pop(0)
        return max_length
                
