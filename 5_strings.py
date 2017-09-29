s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = s.upper()
s = s.replace('.', '')
s = s.replace(',', '')
s = s.replace('\n', '')

# print(s)
word_list = s.split(' ')
# print(word_list)

unique_words = []
for word in word_list:
    if word not in unique_words:
        unique_words.append(word)

# print(unique_words)
unique_words.sort()
# print(unique_words)
for word in unique_words:
    print(word)
