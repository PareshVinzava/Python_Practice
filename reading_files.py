text_file = open("/home/paresh/text.txt", "r")
# print(text_file.readable())
# print(text_file.read())
print(text_file.readline())
print(text_file.readline())
print(text_file.readline()[2])
text_file.close()

text_file = open("/home/paresh/text.txt", "r")
for words in text_file.readlines():
    print(words)
text_file.close()