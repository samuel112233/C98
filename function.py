def countWordsFromFile():
    fileName=input('Enter the file name ')
    file=open(fileName,'r')
    numberOfWords=0
    for line in file:
        words=line.split()
        print(len(words))
        numberOfWords=numberOfWords+len(words)
        print('number of words in your file are ',numberOfWords)

countWordsFromFile()
