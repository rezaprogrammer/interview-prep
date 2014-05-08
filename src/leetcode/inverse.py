'''
Created on May 7, 2014

@author: vsa
'''


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        l = len(s)
        ss = list(s)
        for i in range(int(l/2)):
            ss[i], ss[l-i-1] = ss[l-i-1], ss[i]
            
        j = 0
        for i in range(l):
            if ss[i] == ' ':
                for k in range(0, i-j+1):
                    ss[j+k], ss[i-k] = ss[i-k], ss[j+k]
                j = i
                
        return ''.join(ss)

if __name__ == '__main__':
    s = 'Hello Reza'
    solution = Solution()
    r = solution.reverseWords(s)
    
    print(s)
    print(r)
    
    pass