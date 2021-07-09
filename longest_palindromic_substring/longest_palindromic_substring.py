# WORKS BUT NEEDS TO BE OPTIMIZED
# 
# def is_palindrome(string):
#         reverse = string[::-1]
#         if string.lower() == reverse.lower():
#             return True
#         else:
#             return False

# def longestPalindrome(s):

#         lista = []
#         palindromes = []
#         count = 0
#         length = int(len(s))
        
#         while count < length:
            
#             lista.append(s[count])
            
#             if int(len(lista)) > 1:
#               palindrome_possibly = ''.join([str(elem) for elem in lista])
#               if is_palindrome(palindrome_possibly):
#                 palindromes.append(palindrome_possibly)
                
            
#             count += 1
            
#             if count == length:
#                 count = 0
#                 length -= 1
#                 lista.clear()
#                 s = s[1:]
#                 if int(len(s)) == 1:
#                   break
        
#         return max(palindromes, key=len)
        
# print(longestPalindrome('babad'))
# print(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))

# another example which works but needs to be optimized

def is_palindrome(string):
        reverse = string[::-1]
        if string.lower() == reverse.lower():
            return True
        else:
            return False

def longestPalindrome(s):
        if int(len(s)) == 1:
          return s


        word = ""
        word_length = 0
        start = 0
        end = 2
        original_end = 2
        
        length = int(len(s))

        while start < length:
            
            if is_palindrome(s[start:end]):
              
              
              if int(len(s[start:end])) > word_length:
                word = s[start:end]
                word_length = int(len(word))

            end += 1

            if end > length:
              start += 1
              original_end += 1
              end = original_end
              
            
            

        return word
              
print(longestPalindrome('a'))
        
