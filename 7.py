commands = str(input())
point = str(input())
list_coor_point = point.split()
x = int(0)
y = int(0)
c = False
for i in range(len(commands)):
    if commands[i] == "L":
        x -= 1
    elif commands[i] == "R":
        x += 1
    elif commands[i] == "U":
        y += 1
    elif commands[i] == "D":
        y -= 1
    if x == int(list_coor_point[0]) and y == int(list_coor_point[1]):
        c = True
        print("Passed")
        break
if c == False:
    print("Missed")