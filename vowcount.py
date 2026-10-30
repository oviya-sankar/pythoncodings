a=input("Enter a string:")
count=0
vowels="aeiou"
for i in a.split():
    if i[0] in vowels:
        count+=1
print("words starting with vowels:",count)        
output:
Enter a string:aeiou is a vowels
words starting with vowels: 3


