jewels=input("Enter jewels:")
stones=input("Enter stones:")
count=0
for i in stones:
    if i in jewels:
        count+=1
print(count)   
output:
Enter jewels:ol
Enter stones:hello world
5

