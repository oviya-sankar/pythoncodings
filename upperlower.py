s = input("Enter a string: ")
result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()

print("Converted string:", result)
output:
Enter a string: helloWORld
Converted string: HELLOworLD
