# lab 21 - count_words.py

import os, string

def count_words(words):
    """
    returns tuple (unigrams, bigrams) of single word counts (unigrams) and successive word pair counts (bigrams)
    unigrams: dict of word:count pairs with stopwords (common, non-informative english words) removed
    bigrams: dict of bigram:count pairs with stopwords removed
    """
    STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', 'one', 'gutenbergtm', 'gutenberg']
    unigram_count = {}
    bigram_count = {}

    for i in range(len(words)):
        word = words[i]
        if word not in STOPWORDS:  # ignore stopwords
            # increase count if the word exists, else set count as 1
            unigram_count[word] = unigram_count.get(word, 0) + 1
        if i < len(words) - 1:  # bigram check
            if (words[i] not in STOPWORDS) and (words[i+1] not in STOPWORDS):
                bigram = (words[i], words[i+1])
                bigram_count[bigram] = bigram_count.get(bigram, 0) + 1
    return (unigram_count, bigram_count)


def clean_text(text):
    """
    returns list of words that have been converted to lowercase and stripped of punctuation
    """
    translator = str.maketrans('', '', string.punctuation)
    no_punct = text.translate(translator)
    return no_punct.lower().split()


def most_frequent(counter, num=10):
    """
    prints the num most frequent entries in the counter
    """
    counter = list(counter.items())
    counter.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(num, len(counter))):  # print the top 20 words, or all of them, whichever is smaller
        print(counter[i])


if __name__ == '__main__':
    book_dir = 'books'
    for file_name in os.listdir(book_dir):
        if file_name.endswith('.txt'):
            with open(os.path.join(book_dir, file_name), encoding='utf-8') as book:
                print('-'*48)
                print(f'Reading {file_name}...')
                print('-'*48)
                text = book.read()

            # generate counters
            unigram_count, bigram_count = count_words(clean_text(text))

            # print top 20 words
            print('-'*48)
            print('Most common words: ')
            print('-'*48)
            most_frequent(unigram_count, 20)

            # print top 20 bigrams
            print('-'*48)
            print('Most common pairs: ')
            print('-'*48)
            most_frequent(bigram_count, 20)

            print()