from functools import reduce

def count_words(doc):
    normalized_doc = "".join(c.lower() if c.isalpha() else " " for c in doc)
    frequencies = {}
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies

def combine_counts(d1,d2):
    d = d1.copy() # why exactly was a copy needed here?
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count

    return d


c = count_words("It was the best of times, it was the worst of times!")
print(c)

documents = ["It was the best of times, it was the worst of times",
             "I went to the woods because I wished to live deliberately",
             "Friends, Romans, Countrymen, lend me your ears",
             "I do not like Green Eggs and Ham, I do not like them, Sam-I-am"]

counts = map(count_words, documents)

total_counts = reduce(combine_counts, counts)
print(total_counts)


# consider that counts is a collection of dictionaries, each containing word-counts
# total_counts is then a single dictionary with the total counts
# because as reduce goes through the sequence of dicts in counts, 
# it is accumulating them two dicts at a time using combine_counts, until it reaches end.

