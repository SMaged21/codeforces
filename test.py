# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**(1/2)) + 1):
#         if n % i == 0:
#             return False
#     return True

# def count_divisors(n):
#     count = 0
#     for i in range(1, int(n**(1/2)) + 1):
#         if n % i == 0:
#             count += 1
#             if n // i != i:
#                 count += 1
#     return count

# def main():
#     n = int(input(""))
#     li = list(map(int, input("").split()))
#     li.sort()
#     mx = li[-1]
#     mn = li[0]
#     palindrome_count = 0
#     prime_count = 0
#     max_divisor = li[0]
#     max_div_count = count_divisors(max_divisor)

#     for num in li:
#         if is_palindrome(num):
#             palindrome_count += 1
#         if is_prime(num):
#             prime_count += 1
#         num_div_count = count_divisors(num)
#         if num_div_count >= max_div_count:
#             max_div_count = num_div_count
#             max_divisor = num

#     print("The maximum number : ", mx)
#     print("The minimum number : ", mn)
#     print("The number of prime numbers : ", prime_count)
#     print("The number of palindrome numbers : ", palindrome_count)
#     print("The number that has the maximum number of divisors : ", max_divisor)

# if __name__ == "__main__":
#     main()


# n,shift=map(int,input("").split())
# li=list(map(int,input("").split()))
# li2=[0]*n
# for i in range(n):
#         index=(i+shift)%n
#         li2[index]=li[i]
   
# for i in li2:
#     print(i,end=" ")
          


         
     
# t=int(input(""))
# for i in range(t):
#      li=[]
#      n=int(input(""))
#      for j in range(n):
#         s=input("")
#         index=s.find("#")
#         li.append(index+1)
#      for j in range(n):
#          print(li.pop(),end=" ")
#      print(end="\n")



#---------------------8 Neighbors---------------------------------------


# N,M=map(int,input("").split())
# li=["x"*(M+2)]*(N+2)
# for i in range(1,N+1):
#     s=input("")
#     s="x"+s+"x"
#     li[i]=s

# X,Y=map(int,input("").split())

# if  li[X+1][Y]=="." or li[X-1][Y]=="." or li[X][Y+1]=="." or li[X][Y-1]=="." or li[X-1][Y-1]=="." or li[X+1][Y+1]=="." or li[X-1][Y+1]=="." or li[X+1][Y-1]==".":
#     print("no")
# else:
#     print("yes")





#------------------------------Mirror Array----------------------------



# rows,cols=map(int,input("").split())
# li=[]
# for i in range(rows):
#     col=list(map(int,input("").split()))
#     li.append(col[::-1])

# for i in range(rows):
#     for j in range(cols):
#         print(li[i][j],end=" ")
#     print(end="\n")


#------------------Frequency array------------------------------


# N,M=map(int,input("").split())
# li1=list(map(int,input("").split()))
# li2=[0]*(M+1)
# for i in li1:
#     li2[i]+=1
# for j in range(1,M+1):
#     print(li2[j])



#------------- is b a subsequence of A-------------------------------------------

# N,M=map(int,input("").split())
# s1=list(map(int,input("").split()))
# s2=list(map(int,input("").split()))
# i=0
# j=0
# while i<N and j<M:
#     if s1[i]==s2[j]:
#         j+=1
#     i+=1
# if j!=M:
#     print("NO")
# else:
#     print("YES")

#------------------------permutation with arrays------------------------------------


# n=int(input(""))
# s1=list(map(int,input("").split()))
# s2=list(map(int,input("").split()))
# s1.sort()
# s2.sort()
# if s1==s2:
#     print("yes")
# else:
#     print("no")



#----------------count subarrays----------------------
# t=int(input(""))
# for i in range(t):
#     li2=[]
#     n=int(input(""))
#     li=list(map(int,input().split()))

#     count1=1
#     count2=0
#     start=0

#     li2=[]
#     for j in range(1,n):
        
#         if li[j]>=li[j-1]:
#            count1+=1 
#         else:
#             li2.append(count1)
#             count1=1
#             start=j
#     li2.append(count1)
 
#     if len(li)==1:
#         print(1)
#     else:
        
#         for m in li2:
#             count2+=(m*(m+1))/2
#         print(int(count2))
#--------------------watermelon--------------------------------
# w=int(input(""))
# if w==2 or w%2==1:
#     print("NO")
# else:
#     print("YES")
#------------------------------wrong subtraction---------------
# n,t=map(int,input("").split())
# for _ in range(t):
#     if n % 10 !=0:
#         n-=1
#     else:
#         n/=10
# print(int(n))
#-----------------------Hit lottery-----------------------------

# n=int(input(""))
# count=0
# while n!=0:
#     if n>=100:
#         n-=100
#     elif n>=20:
#         n-=20
#     elif n>=10:
#         n-=10
#     elif n>=5:
#         n-=5
#     elif n>=1:
#         n-=1
#     count+=1
# print(count)

#-----------------------Elephant------------------
# n=int(input(""))
# count=0
# while n!=0:
#     if n>=5:
#         n-=5
#     elif n>=4:
#         n-=4
#     elif n>=3:
#         n-=3
#     elif n>=2:
#         n-=2
#     elif n>=1:
#         n-=1
#     count+=1
# print(count)
#-------------------Food buying ------------------------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     container = n
#     while container >=10:
#         n=n+container//10
#         container=container%10+container//10
#     print(n)
#--------------------power two-----------------------------
# n=int(input(""))
# f=True
# while n!=1:
      
#       r=n%2
#       if r!=0:
#             f=False
#             break
#       n/=2
# if f:
#       print("YES")
# else:
#       print("NO")
#---------------------prime checking------------------
# n=int(input(""))
# if n==1:
#     print("NO")
# else:
#     for i in range(2,int(n**(1/2))+1):
#         if n%i==0:
#             print("NO")
#             break
#     else:
#         print("YES")
#----------sum of range---------------------
# def sumo(n):
#     res = (n + 1) // 2
#     return res * res

# def sume(n):
#     return n * (n + 1)

# n1, n2 = map(int, input("").split())
# mx = max(n1, n2)
# mn = min(n1, n2)
# even = sume(mx // 2) - sume((mn - 1) // 2)
# odd = sumo(mx) - sumo(mn - 1)
# s = even + odd
# print(int(s))
# print(int(even))
# print(int(odd))


#----------------Distinct number-----------------
# n=int(input(""))
# res=int((-1+(1+8*n)**(1/2))/2)
# print(res)

#---------------------convert to base-----------------
# T=int(input(""))
# N,X=map(str,input("").split())
# X=int(X)
# res=0
# res2=""
# if T==1:
#     N=N[::-1]
#     for i in range(len(N)):
#         if N[i].isalpha():
#              res += (X ** i) * (ord(N[i]) - 55) 
#         else: 
#             res += (X ** i) * int(N[i]) 
#     print(res)
# else:
#     N=int(N)
#     while N!=0:
#         if N%X<10:
#             res2=str(N%X)+res2
#         else:
#             res2=chr((N%X)+55)+res2
#         N=int(N/X)
#     print(res2)
    






#-----------------permutation and combination-------------------
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)

# def permutation(n, r):
#     p = fact(n) // fact(n - r)
#     c = p // fact(r)
#     return int(p), int(c)

# n, r = map(int, input().split())

# p, c = permutation(n, r)
# print(c, p)

#-------------Two lines-------------------------
# x1,y1,x2,y2=map(int,input("").split())
# x3,y3,x4,y4=map(int,input("").split())
# if x2-x1==0 and x4-x3==0:
#     print("YES")
# elif (x2 - x1 == 0 or x4 - x3 == 0): 
#     print("NO")
# elif (y2-y1)/(x2-x1)==(y4-y3)/(x4-x3):
#     print("YES")
# else:
#     print("NO")
#--------------strait line---------------------
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())

# if (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1):
#     print("YES")
# else:
#     print("NO")
#------------GCD------------------------------
# def gcd(n, m):
#     if m == 0:
#         return n
#     else:
#         return gcd(m, n % m)

# def lcm(n, m): return abs(n * m) // gcd(n, m)


# n,m=map(int,input("").split())

# print(gcd(n,m),lcm(n,m))
#-------------------Divisible--------------------

# N, X = input().split()
# X = int(X)

# remainder = 0
# for digit in N:
#     remainder = (remainder * 10 + int(digit)) % X


# if remainder == 0:
#     print("YES")
# else:
#     print("NO")

#----------------Divisability--------------
# A, B, X = map(int, input().split()) 
# mx = max(A, B)
# mn= min(A, B)
# A=mn
# B=mx

# if A % X != 0:
#      A = A + (X - A % X) 
# if B % X != 0:
#      B = B -(B% X) 
# ANS=(A+B)*(B-A+X)/(2*X)
# print(int(ANS))

#---------------Multiplication of matrices------------------------------
# m, n = map(int, input().split())
# m1 = []
# for i in range(m):
#     r = list(map(int, input().split()))
#     m1.append(r)

# x, y = map(int, input().split())
# m2 = []
# for i in range(x):
#     r = list(map(int, input().split()))
#     m2.append(r)


# res = [[0 for _ in range(y)] for _ in range(m)]


# for i in range(m):
#     for j in range(y):
#         for k in range(n):
#             res[i][j] += m1[i][k] * m2[k][j]


# for i in range(m):
#     for j in range(y):
#         print(res[i][j], end=' ')
#     print()
#-----------------summtion of its divisors--------------
# def sum_of_divisors(N): 
#     total = 0 
#     for i in range(1, int(N**0.5) + 1): 
#         if N % i == 0 : 
#             total += i 
#             if i != N // i: 
#                 total += N // i 
#     return total 
    

# N = int(input()) 
# print(sum_of_divisors(N))


#--------------product----------
# def product_modulo(L, R, M):
#     product = 1
#     for i in range(L, R + 1):
#         product = (product * i) % M
#     return product

# L, R, M = map(int, input().split())
# print(product_modulo(L, R, M))
#--------------------prime factors----------------------------------------
# n=int(input(""))
# res=""
# f=False
# for i in range(2,int(n**(1/2))):
#     if n%i==0:
#         count=0
#         f=True
#         while n%i==0:
#             n/=i
#             count+=1
#         res+=f"({i}^{count})*"
# if f:
#     print(res[0:len(res)-1])
# else:
#     print(f"({n}^1)")


#---------my First sorting problem--------------------------
# t=int(input(""))
# for _ in range(t):
#     x,y=map(int,input("").split())
#     if x<y:
#         print(x,y)
#     else:
#         print(y,x)

#------------------Sasha and array coloring-----------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     li=list(map(int,input("").split()))
#     li.sort()
#     j=n-1
#     sum=0
#     for i in range(n//2):
#         sum+=li[j]-li[i]
#         j-=1
#     print(sum)
#------------------verify password------------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     s=input("")
#     f=False
#     for i in range(1,n):
#         if ord(s[i]) < ord(s[i-1]):
#             f=True
#             break
#     if f:
#         print("NO")
#     else:
#         print("YES")

#------------------------X axis------------------------
# t=int(input(""))
# for _ in range(t):
#     li=list(map(int,input("").split()))
#     li.sort()
#     print((li[1]-li[0])+(li[2]-li[1]))
#------------------Increasing------------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     li=list(map(int,input("").split()))
#     st=set(li)
#     if len(li)!= len(st):
#         print("NO")
#     else:
#         print("YES")

#------------------only Pluses-----------------
# t=int(input(""))
# for _ in range(t):
#     li=list(map(int,input("").split()))
#     li.sort()
#     a=li[0]
#     b=li[1]
#     c=li[2]
#     for i in range(5):
#         if a<= b and a<=c :
#             a+=1
#         else:
#             if b<=c:
#                 b+=1
#             else:
#                 c+=1
#     print(a*b*c)
#--------------Oath of the Night's Watch------------
# n=int(input(""))
# li=list(map(int,input("").split()))
# if n<3:
#     print(0)
# else:
#     li.sort()
#     mn=li[0]
#     mx=li[n-1]
#     c=0
#     for i in range(1,n-1):
#         if li[i]> mn and li[i]<mx:
#             c+=1
#     print(c)
  
#-------------------------T. Polycarp Training-------------
# n=int(input(""))
# li=list(map(int,input("").split()))
# li.sort()
# c=0
# for i in li:
#     if i>= c+1:
#         c+=1
# print(c)
#-----------------------Advantage---------------------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     li=list(map(int,input("").split()))
#     mx=max(li)
#     if li.count(mx)>1:
#         for i in li:
#             print(i-mx,end=" ")
#     else:
#         for i in li:
#             if i==mx:
#                 print(i-max(set(li)-{mx}),end=" ")
#             else:
#                 print(i-mx,end=" ")
#     print()

#-------------------------------Maximize the score ------------------------------------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     score=0
#     li=list(map(int,input("").split()))
#     li.sort()
#     for i in range(n):
#         score+=min(li[0],li[1])
#         li.pop(1)
#         li.pop(0)
#     print(score)

#--------------------H. Submission Bait------------
# def alice_wins(n, a):
#     if n%2==0:
#         a.sort(reverse=True)
#     else:
#         a.sort()
#     mx = 0
#     moves = 0
#     for i in range(n):
#         if a[i] >= mx:
#             mx = a[i]
#             a[i] = 0
#             moves += 1
#         else:
#             break
#     if moves % 2 == 1:
#         return "YES"
#     else:
#         return "NO"

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(alice_wins(n, a))




#-----------------------------Sereja and Dima------------------
# n=int(input(""))
# li=list(map(int,input("").split()))
# seraja=0
# dima=0
# i=0
# while len(li)!=0:

#     if li[0]>=li[len(li)-1]:
#         mx=li.pop(0)
#     else:
#         mx=li.pop()
#     if i % 2==0:
#         seraja+=mx
#     else:
#         dima+=mx
#     i+=1
# print(seraja,dima)
#----------------------ICPC Balloons----------------------
# t=int(input(""))
# for _ in range(t):
#     sl=int(input(""))
#     s=input("")
#     li=[]
#     sum=0
#     for i in range(sl):
#         if s[i] in li:
#             sum+=1
#         else:
#             sum+=2
#             li.append(s[i])
#     print(sum)
#------------------- Regular Bracket Sequence---------
# s=input("")
# li=[]
# count=0
# for b in s:
#     if b=="(":
#         li.append(b)
#     else:
#         if  len(li)!=0 and li[len(li)-1] :
#             li.pop()
#             count+=1
# print(count*2)

#----------------------E. Snacktower----------------------
# n=int(input(""))
# li=list(map(int,input("").split()))
# li2=[]
# for i in range(n):
#     li2.append((li[i],i))
# li2.sort(reverse=True)
# i=0
# j=0
# while i< n:
#     while li2[i][1]<=j :
#         print(li2[i][0],end=" ")
#         i+=1
#         if i==n:
#             break
#     else:
#         print()
#     j+=1




#---------------Eating candies-------------------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     li=list(map(int,input("").split()))
#     Alice=0
#     Bob=0
#     i=0
#     j=n-1
#     Alicec=li[i]
#     Bobc=li[j]
#     while i<j:
#         if Alicec==Bobc:
#             Alice=i+1
#             Bob=n-j
#             i+=1
#             j-=1
#             Bobc+=li[j]
#             Alicec+=li[i]

#         elif Alicec>Bobc:
#             j-=1
#             Bobc+=li[j]
            
#         else:
#             i+=1
#             Alicec+=li[i]
            
#     print(Alice+Bob)
#---------------chat order--------------
# n=int(input())
# chatOrder={}
# for i in range(n):
#     chat=input("")
#     chatOrder[chat]=i
# li=[]
# for key in chatOrder:
#     li.append((chatOrder[key],key))
# li.sort(reverse=True)
# for i in li:
#     print(i[1])
#--------------potions----------------
# n=int(input(""))
# li=list(map(int,input("").split()))
# count=0
# s=0
# n=[0]
# for e in li:
#     if e>=0:
#         s+=e
#         count+=1
#     else:
#         if s+e>=0:
#             count+=1
#             s+=e
#             n.append(e)
#         else:
#             n.sort()
#             if e>n[0]:
#                 s-=n[0]
#                 n.pop(0)
#                 s+=e
#                 n.append(e)
# print(count)

        
#----------------Powering the hero----------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     army=0
#     bonus=[0]
#     li=list(map(int,input("").split()))
#     for e in li:
#         if e==0 and bonus[0]!=0:
#             army+=bonus[0]
#             bonus.pop(0)
#         else:
#             bonus.append(e)
#             bonus.sort(reverse=True)
            
#     print(army)

#------------S. YetnotherrokenKeoard-----------------
# t = int(input())
# for _ in range(t):
#     s = input()
#     c = []
#     sm = []
    
#     for i in range(len(s)):
#         if s[i] == "b":
#            if sm: 
#              sm.pop()
#         elif s[i]=="B":
#             if c:
#                 c.pop()
#         else:
#             if s[i].islower():
#                 sm.append((i, s[i]))
#             else:
#                 c.append((i, s[i]))
    
#     combined = sm + c
#     combined.sort()
#     s2 = "".join([char for _, char in combined])
    
#     print(s2)


#-------------Era--------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     li=list(map(int,input("").split()))
#     lst=[]
#     for i in range(1,n+1):
#         lst.append((i,li[i-1]))
#     c=0
#     for e in lst:
#         if e[1]>e[0]:
#             if c<e[1]-e[0]:
#                 c=e[1]-e[0]
#     print(c)
   
#-----------------String similarity---------------
# t=int(input(""))
# for _ in range(t):
#     n=int(input(""))
#     s=input("")
#     li=[]
#     for i in range(n):
#         li.append(s[i:n+i])
#     r=""
#     for i in range(n):
#         r+=li[i][i]
#     print(r)
#-----------E. Vasilije in Cacak
# t=int(input(""))
# for _ in range(t):
#     n,k,x=map(int,input("").split())
#     mn=(k*(k+1))/2
#     mx=((n*(n+1))/2)-((n-k)*(n-k+1)/2)
#     if x >= mn and x<=mx:
#         print("YES")
#     else:
#         print("NO")

        

#------------------B. Andryusha and Socks-------
# n=int(input(""))
# li=list(map(int,input("").split()))
# st=set(li[:n])
# print(len(st))

 
    


    







        




















    






            







        












