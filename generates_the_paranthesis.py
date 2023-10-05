res=[]
def bt(s,open=0,close=0):
    if open==close==n:
        res.append(s)
    if open<n:
        bt(s+"(",open+1,close)
    if close<open:
        bt(s+")",open,close+1)
    return res
n=int(input())
result=bt(s="")
for p in result:
    print(p,end='')
#print(p)
    