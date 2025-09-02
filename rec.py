#-------------Love A------------------
# s=input()
# ac=s.count("a")
# l=len(s)-ac

# if ac > l:
#     print(len(s))
# else:
#     print(ac*2-1)

#-----------------Primary task----------------
# t=int(input(""))
# for i in range(t):
#     s=input()
#     if len(s)<3:
#         print("NO")
#     else:
#         n=s[0:2]
#         if n!="10":
#             print("NO")
#         else:
#             r=s[2::]
#             if r[0]=="0":
#                 print("NO")
#             elif int(r)<2:
#                 print("NO")
#             else:
#                 print("YES")


#-------------------------------Insert Digit-------------------
# t=int(input(""))
# for _ in range(t):
#     n,d=map(int,input("").split())
#     d=str(d)
#     s=input("")
#     f=False
#     for i in range(n):
#         if s[i]<d:
#             s=s[0:i]+d+s[i::]
#             print(s)
#             f=True
#             break
#     if not(f):
#         print(s+d)
        
            
#--------------------Soldier and Banans---------------------
# K,m,n=map(int,input().split())
# sum=K*(n+1)*n/2
# if sum<=m:
#     print(0)
# else:
#     print(int(sum-m))
#------------------------Profitable interest rate-------------------
# t=int(input(""))
# for i in range(t):
#     a,b=map(int,input("").split())
#     if a>=b:
#         print(a)
#     else:
#         x=b-a
#         if a-x<0:
#             print(0)
#         else:
#             print(a-x)
#--------------I'm bored with life---------------------
# n,m=map(int,input("").split())

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# mn=min(n,m)
# print(fact(mn))
#-------------Little c loves 3 I
# n=int(input(""))


# a=n//3
# b=a
# c=n-2*a
# if a%3==0:
#     a-=1
#     b+=1
#     if b%3==0:
#         b+=1
#         a-=1
# if c%3==0:
#     c-=1
#     b+=1
#     if b%3==0:
#         b+=1
#         c-=1

# print(a,b,c)


#-------------Most similar words----------------------
# t=int(input(""))
# for _ in range(t):
#     li=[]
#     diff=[]
#     n,m=map(int,input("").split())
#     for i in range(n):
#         word=input("")
#         li.append(word)
    
#     for j in range(n):
#         for l in range(j+1,n):
#             word1 = li[j]
#             word2 = li[l]
#             word_diff = sum(abs(ord(c1) - ord(c2)) for c1, c2 in zip(word1, word2))
#             diff.append(word_diff)
#     print(min(diff))





