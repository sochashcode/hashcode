# crude solution just using horizontal lines
import sys

if len(sys.argv) != 2:
    print "pass .in file as arg"
    sys.exit(0)

fn = sys.argv[1]

f = open(fn, "r").readlines()
(rows,cols) = map(int, f[0].strip().split(" "))
data = f[1:]

def isFill(r,c):
    return data[r][c] == '#'

cmds = []
for row in range(rows):
    col = 0
    while col<cols:
        if(isFill(row,col)):
            start = col
            end = start
            while col<cols and isFill(row,col):
                col+=1
            cmds.append("PAINT_LINE %d %d %d %d" % (row,start,row,col-1))
        col += 1

print len(cmds)
for c in cmds:
    print c

