words=input()
result=[].split()
for i in words:
    for j in words:
     if i!=j and i in j:
         result.append(i)
         break
print(result)
output:
mass as hero superhero
['as', 'hero']


        
