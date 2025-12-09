string=input("enter the string:")
char_count=0
for ch in string:
    char_count=char_count+1
word_count=0
for ch in string:
    if ch==" ":
        word_count=word_count+1
print(char_count)
print(word_count)