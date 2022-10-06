# Дан текст: в первой строке записано число строк, далее идут сами строки. 
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.

n = int(input())
A = set()
for i in range(n):
    S = input().split()
    for elem in S:
        A.add(elem)
print(len(A))