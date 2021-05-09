f=open('Samuel.txt')
filelines=f.readlines()
for line in filelines:
    print(line)

intro='Hi I am Samuel, I love coding.'
words=intro.split(',')
print(words)
def greet(name):
    print('Hello, '+name+'.How are you')

greet('Samuel')