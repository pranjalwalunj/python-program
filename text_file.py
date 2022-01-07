# f = open('Untitled.txt', 'w')
# f.write("\n")

lines = ['Untitled', 'how to write text file in python']
with open('Untitled.txt', 'w') as f:
    for line in lines:
        f.writelines(lines)




