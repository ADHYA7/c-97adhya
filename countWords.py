intro=input('enter about yourself: ')
charectercount=0
wordcount=1
for i in intro:
    charectercount=charectercount+1
    if (i ==' '):
        wordcount=wordcount+1
print(charectercount)
print(wordcount)