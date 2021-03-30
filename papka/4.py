import re
txt = "The rain in Spain"
x = re.sub("\s", "123", txt, 2)
print(x)