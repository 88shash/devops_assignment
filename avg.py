import sys

fname = sys.argv[1]
my_list = []

with open(fname, 'r') as f:
    for i in f.readlines():
        my_list.append(int(i))
        
avg = sum(my_list)/len(my_list)

print(avg)