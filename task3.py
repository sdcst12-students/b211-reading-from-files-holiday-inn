#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""
filename = 'task03.txt'
file = open(filename,'r')
data = file.read()
data = data.split('\n\n')
new=[]
poo = []
for i in data:
    i = i.split('\n')
    new.append(i)
new.pop(-1)
data = new
for i in data:
    num = 0
    for j in i:
        j = int(j)
        num+=j
    poo.append(num)
print(poo)
num1 = 0
for i in poo:
    if i > num1:
        num1 = i
print(num1)
