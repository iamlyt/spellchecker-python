dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

# split the input (this turns into a list)
user_input = input().split()

# create a list to store misspelled words
misspelled_words = []

# iterate through each word in the user_input and add the misspelled words into the list
for word in user_input:
    if word not in dictionary:
        misspelled_words.append(word)

# if misspelled_words list is not empty, print each words and separate by line
if misspelled_words:
    print(*misspelled_words, sep='\n')
# otherwise, print 'OK'
else:
    print("OK")
