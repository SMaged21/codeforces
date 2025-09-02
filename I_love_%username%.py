n=int(input())
li=list(map(int,input().split()))
max=min=li[0]
a=0
for i in range(1,n):
    if li[i]<min:
        min=li[i]
        a+=1
    elif li[i]>max:
        max=li[i]
        a+=1
print(a)

