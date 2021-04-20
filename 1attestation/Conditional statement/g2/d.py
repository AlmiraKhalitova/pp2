a=input()
X, Y= map(int, input().split())
x=0
y=0

for i in range(len(a)):
    if a[i]=='L': x-=1
    if a[i]=='R': x+=1
    if a[i]=='U': y+=1
    if a[i]=='D': y-=1

    if x>X and y>=Y:
        print("Passed") 
        exit()
    elif y>Y and x>=X:
        print("Passed") 
        exit()

print("Missed")   
