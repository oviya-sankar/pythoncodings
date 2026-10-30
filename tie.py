s = input("Enter a string: ")
max_count = 0
for ch in s:
    count = s.count(ch)
    if count > max_count:
        max_count = count
        result = ch
print("Most frequent character:", result)
