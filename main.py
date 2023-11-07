dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

user_input = input().split()

misspelled_words = []

for word in user_input:
    if word not in dictionary:
        misspelled_words.append(word)

if misspelled_words:
    print(*misspelled_words, sep='\n')
else:
    print("OK")
