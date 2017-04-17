__author__ = 'Tom Stanley'
stringDict = {}
string = input("Enter your string:").lower().split()
for word in string:
    if word in stringDict:
        stringDict[word] += 1
    else:
        stringDict[word] = 1
longest_word_len = 0
for key in stringDict:
    current_word_len = len(key)
    if current_word_len > longest_word_len:
        longest_word_len = current_word_len
sorted_string_dict = (sorted(stringDict))
for word in sorted_string_dict:
    print("{:{}} : {}".format(word, longest_word_len, stringDict.get(word)))
