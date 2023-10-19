"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
filename = 'task02c.txt'
file = open(filename,'r')
data = file.read()
data = data.split('\n\n')
new=[]
for i in data:
    i = i.split('\n')
    new.append(i)
new.pop(-1)
data = new
print(data)
tally = 0
for i in data:
    i[0] = int(i[0])
    i[1] = int(i[1])
    i[2] = int(i[2])
    mini = min(i)
    maxi = max(i)
    
    mid = (int(i[1])+int(i[2])+int(i[0])) - int(mini) - int(maxi)

    if (mini**2 + mid**2) == maxi**2:
        print(maxi,mid,mini," works")
        tally+=1
    else: print(maxi,mid,mini," does not work")
print(f"There are {tally} Pythagorean triangles")

