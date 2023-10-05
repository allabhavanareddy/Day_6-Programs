def toh(n,sour,aux,des):
    if n>0:
        toh(n-1,sour,des,aux)
        print(sour,des)
        toh(n-1,aux,sour,des)
n=int(input())
toh(n,'a','b','c')
 
#towers of hanoi count
count=0
def toh(n,src,aux,des):
    global count
    if n==1:
       count=count+1
       return
    toh(n-1,src,des,aux)
    count=count+1
    toh(n-1,aux,src,des)
n=int(input())
src,aux,des='a','b','c'
toh(n,src,aux,des)
print(count)