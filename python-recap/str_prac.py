
import string
import random

def generate_password(length=12):
    # Combine lowercase, uppercase, digits, and symbols
    pool = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters from the pool
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

# print(generate_password()) #

# print(string.punctuation)

text='hello jagadeesh,hello jagadeesh,jagadeesh is such a good guy;'
table = str.maketrans(string.punctuation, ' ' * len(string.punctuation)) 
clean_text=text.translate(table)


words=clean_text.split()

d={}

for word in words:
    d[word]=d.get(word,0)+1

popular_word=''
maximum=0
for key,value in d.items():
    # print(j)
    if value>maximum:
        maximum=value
        popular_word=key
print(popular_word)

#             #(or)

# # popular_word = max(d, key=d.get)
# # print(popular_word)

# Split into words

# from collections import Counter

# words = clean_text.split()

# # Count words using Counter
# word_count = Counter(words)
# print(word_count)

# # Get most popular word
# popular_word = word_count.most_common(1)[0][0]
# print(popular_word)  # Output: jagadeesh