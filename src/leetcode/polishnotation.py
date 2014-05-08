'''
Created on May 7, 2014

Link: http://oj.leetcode.com/submissions/detail/6300025/

@author: vsa
'''

class Solution:
    
    def isnumber(self, i):
        if i.startswith('-') or i.startswith('+'):
            return i[1:].isdigit()
        else:
            return i.isdigit()
        
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if len(tokens) == 0:
            return
        
        first = tokens.pop()
        if self.isnumber(first):
            return int(first)
        
        op = first
        v2 = self.evalRPN(tokens)
        v1 = self.evalRPN(tokens)

            
        if op == '*':
            rslt = v1 * v2
        elif op == '-':
            rslt = v1 - v2
        elif op == '+':
            rslt = v1 + v2
        elif op == '/':
            rslt = v1 / v2
        else:
            raise Exception("Unsupported operation {0}".format(op))

        return int(rslt)

if __name__ == '__main__':
    solution = Solution()
    tokens1 = ["2", "1", "+", "3", "*"]
    tokens2 = ["4", "13", "5", "/", "+"]
    tokens3 = ["3","-4","+"]
    tokens4 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    
#     val1 = solution.evalRPN(tokens1)
#     print(val1)
#     
#     val2 = solution.evalRPN(tokens2)
#     print(val2)
# 
#     val3 = solution.evalRPN(tokens3)
#     print(val3)

    val4 = solution.evalRPN(tokens4)
    print(val4)