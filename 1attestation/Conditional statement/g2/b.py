import re
txt=input()
word=input()
a=(re.search(word, txt))
x=bool(re.search(word, txt))
if (x):
    p='First time {} occured in position: {} '
    print(p.format(word,a.start()))
else:
    print ("Not found")