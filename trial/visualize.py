#python2

#parse file as cmd line arg
from Tkinter import *
import sys

if len(sys.argv) != 2:
    print "pass .in file as arg"
    sys.exit(0)

fn = sys.argv[1]

sqSiz =2
f = open(fn, "r").readlines()
(rows,cols) = map(int, f[0].strip().split(" "))
data = f[1:]

master = Tk()

w = Canvas(master, width=cols*sqSiz, height=rows*sqSiz)
w.pack()

for row in range(rows):
    for col in range(cols):
        if(data[row][col] == '#'):
            w.create_rectangle(col*sqSiz, row*sqSiz, (col+1)*sqSiz, (row+1)*sqSiz, fill="blue")


mainloop()
