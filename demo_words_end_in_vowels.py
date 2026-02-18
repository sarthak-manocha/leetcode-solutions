s = "we are learning python"
count = 0

for w in s.split():
    if w[-1] in 'aeiou':
        count += 1

print("Number of words ending with a vowel:", count)