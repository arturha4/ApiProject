words = [i for i in input().split()]  # 0 0 1 2 3 4 0
best = ''
l = 0
for word in words:
    if len(word) > l:
        best = word
        l = len(word)
print(best)
