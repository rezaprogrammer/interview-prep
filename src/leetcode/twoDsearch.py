'''
Created on May 8, 2014

@author: vsa
'''

class Solution:
    def exists(self, board, word, I, J, i, j, visited):
        if len(word)==0:
            return True
        if i<0 or j<0 or i>=I or j>=J:
            return False
        if (i,j) in visited:
            return False
        if board[i][j] != word[0]:
            return False

        visited.add((i,j))        
        c = word.pop(0)
        
        if self.exists(board, word, I, J, i+1, j, visited):
            return True
        if self.exists(board, word, I, J, i, j+1, visited):
            return True
        if self.exists(board, word, I, J, i-1, j, visited):
            return True
        if self.exists(board, word, I, J, i, j-1, visited):
            return True
        
        word.insert(0, c)
        visited.remove((i,j))
        pass


    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        I = len(board)
        J = len(board[0])
        
        for i in range(I):
            for j in range(J):
                if self.exists(board, list(word), I, J, i, j, set()):
                    return True
        return False

if __name__ == '__main__':
    board = [list("ABCE"),
             list("SFCS"),
             list("ADEE")]
    word1 = 'ABCCED'
    word2 = 'SEE'
    word3 = 'ABCB'
    
#     print('{0} exists in board: {1}.'.format(word1, Solution().exist(board, word1)))
    print('{0} exists in board: {1}.'.format(word2, Solution().exist(board, word2)))
#     print('{0} exists in board: {1}.'.format(word3, Solution().exist(board, word3)))
    
    pass