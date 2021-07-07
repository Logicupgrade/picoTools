# Tool for counting word occurences in file

import sys

# input:
# <python_exe> count.py <filename> <word_to_count>

# file name
fName = sys.argv[1]
# word to count
word = sys.argv[2]
#initialize count
wordCount = 0

#read file line by line
with open(fName,'r') as theFile:
    for line in theFile:
        #count word in line and add to wordcount
        wordCount += line.count(word)
print(wordCount)