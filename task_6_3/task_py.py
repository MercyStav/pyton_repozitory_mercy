import collections

with open("jack.txt", "r", encoding='utf-8') as datafile:
    lines = datafile.read()
    words = lines.split()
    words_hist = collections.Counter(words)
    print (words_hist)