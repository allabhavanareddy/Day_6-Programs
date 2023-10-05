#include<stdio.h>
int main()
{
    //write your code here
    int n;
    scanf("%d",&n);
    if(n%2==0)
    {
    return 1;
    }
    generatingmagicsquare(n);
    
    return 0;
}
void generatingmagicsquare(int n)
{
int magicsquare[n][n],i,j;
for(i=0;i<n;i++)
{
for( j=0;j<n;j++)
{
magicsquare[i][j]=0;
}
}

i=n/2;
j=n-1;
int num;
for(num=1;num<=n*n;)
{
if(i==-1 && j==n)
{
i=0;
j=n-2;
}
else
{
if(j==n)
j=0;
if (i<0)
i=n-1;
}
if(magicsquare[i][j])
{
i++;
j-=2;
continue;
    }
else
{
magicsquare[i][j]=num++;
}
i--;
j++;
}
int row,col;
for(row=0;row<n;row++)
{ 
    for(col=0;col<n;col++)
    {
    printf("%d",magicsquare[row][col]);
        if(col<n-1)
        { 
            printf(" ");
        }
    
}
printf("\n");
}
}
