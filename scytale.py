data = ['V', 'P', 'K', 'U', 'E', 'L', 'N', 'C', 'F', 'A', 'S', 'R', 'D', 'I', 'Y', 'H']
joinedData = "". join(data)
wordlength = 4
word = ""

for i in range(wordlength):
    letterIndex = 4 * i + 1
    word += data [letterIndex]

print("Base data   :", joinedData)
print("Hidden word  :", word)