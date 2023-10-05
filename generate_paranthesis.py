l=[]
res=[]
def backtrack(n,opencount=0,closecount=0):
    if opencount==closecount==n:
       res.append("".join(l))
    if opencount<n:
       l.append('(')
       backtrack(n,opencount+1,closecount)
       l.pop()
    if closecount<opencount:
       l.append(')')
       backtrack(n,opencount,closecount+1)
       l.pop()
    return res
n=int(input())
print(backtrack(n))
        