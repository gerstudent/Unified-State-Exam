with open('24-215.txt') as f:
    s = f.readline()

s = s.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
s = s.replace('11A', '*').replace('1', ' ').replace('A', ' ')
print(max(len(x) for x in s.split()))
