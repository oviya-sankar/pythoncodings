s=input()
vowels="aeiou"
c=0
v=0
for i in islower():
 if i.isalpha():
     if i in vowel:
         v+=1
 else:
      c+=1
      print(v,c)
