num=eval(input())
a=[]
for i in num:
  if i!=0:
    a.append(i)
for j in num:
  if j==0:
    a.append(j)       
print(a)    
output:
[0,1,2,0,3]
[1, 2, 3, 0, 0]
