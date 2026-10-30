a=input("Enter a string:")
for ch in a:
    if a.count(ch)==1:
        print("First non repeating character:",ch)
        break
output:
Enter a string:banana
First non repeating character: b
