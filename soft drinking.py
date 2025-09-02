n,k,l,c,d,p,nl,np=map(int,input("").split())
total_drinks=min((k*l)//nl,(p//np),(c*d))//n
print(total_drinks)