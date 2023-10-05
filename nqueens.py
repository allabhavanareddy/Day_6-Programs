class Solution:
    def totalNQueens(self, n):
        col=[]
        podia=[]
        nedia=[]
        board=[["."]*n for i in range(n)]
        ans=[]
        def backtracking(r):
            if r==n:
               l=["".join(i) for i in board]
               ans.append(l)
               return
            for c in range(n):
                if c in col or (r+c) in podia or (r-c) in nedia:
                    continue
                board[r][c]='Q'
                col.append(c)
                podia.append(r+c)
                nedia.append(r-c)
                backtracking(r+1)
                board[r][c]='.'
                col.remove(c)
                podia.remove(r+c)
                nedia.remove(r-c)
        backtracking(0)
        return ans
n=int(input())
a=Solution()
print(a.totalNQueens(n))