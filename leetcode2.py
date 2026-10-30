words=input()
result=[]
for i in words:
    for j in words:
     if i!=j and i in j:
         result.append(i)
         break
print(result)

        
