#!/usr/bin/env python3.5
#coded by ogcyb3r
#updated:2020/04/04
import os
import itertools
import math
from random import randint
myDirpath = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))+'/t4mp'
def cleanme():
    clx='clear'
    os.system(clx)
def randomPWDUpper(list_inputs,minlen,fileSavePath):
	f = []
	for x in range(1,len(list_inputs)+1):
		f = f + list(itertools.permutations(list_inputs,r=x))
	t = []
	for x in range(len(f)):
		if len(''.join(f[x])) >= minlen :
			t.append(''.join(f[x]))
	print("[\x1b[30;38;5;155m+\x1b[0m]\x1b[30;38;5;155m File has been saved in : \x1b[0m \x1b[1;38;5;255mt4mp/%s \x1b[0m"%(fileSavePath))
	if not os.path.exists(myDirpath):
		os.makedirs(myDirpath)
	file_path = "{}/{}".format(myDirpath, fileSavePath)
	f = open(file_path, 'w')
	z = set()
	for x in t:
		z.update(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in x))))
	t = list(z)
	t.sort()
	t.sort(key=len)
	for x in t:
			f.write(x)
			f.write('\n')
	f.close()
def randomPWDLower(list_inputs,minlen,fileSavePath):
	f = []
	for x in range(1,len(list_inputs)+1):
		f = f + list(itertools.permutations(list_inputs,r=x))
	t = []
	for x in range(len(f)):
		if len(''.join(f[x])) >= minlen :
			t.append(''.join(f[x]))
	print("[\x1b[30;38;5;155m+\x1b[0m]\x1b[30;38;5;155m File has been saved in : \x1b[0m \x1b[1;38;5;255mt4mp/%s \x1b[0m"%(fileSavePath))
	if not os.path.exists(myDirpath):
		os.makedirs(myDirpath)
	file_path = "{}/{}".format(myDirpath, fileSavePath)
	f = open(file_path, 'w')
	z = set()
	for x in t:
		z.update(map(''.join, itertools.product(*((c.lower()) for c in x))))
	t = list(z)
	t.sort()
	t.sort(key=len)
	for x in t:
			f.write(x)
			f.write('\n')
	f.close()
def upper(list_inputs,fileSavePath):
	minlen = int(input('[\x1b[30;38;5;155m+\x1b[0m]\x1b[30;38;5;226m Minimum length of a password or hit enter for (\x1b[30;38;5;160m6\x1b[30;38;5;244m) : \x1b[0m') or 6 )
	randomPWDUpper(list_inputs,minlen,fileSavePath)
def lower(list_inputs,fileSavePath):
	minlen = int(input('[\x1b[30;38;5;155m+\x1b[0m]\x1b[30;38;5;244m Minimum length of a password or hit enter for (\x1b[30;38;5;160m6\x1b[30;38;5;244m) : \x1b[0m') or 6 )
	randomPWDLower(list_inputs,minlen,fileSavePath)
def main():
    cleanme()
    print(("""\x1b[1;38;1;239m                         ██
 ██████                 ░██
░██░░░██ ███     ██     ░██
░██  ░██░░██  █ ░██  ██████
░██████  ░██ ███░██ ██░░░██
░██░░░   ░████░████░██  ░██
░██      ███░ ░░░██░░██████
░░      ░░░    ░░░  ░░░░░░randomlly\x1b[0m

[ + ]\x1b[30;38;5;155m Creating password randomlly \x1b[0m
[ + ]\x1b[30;38;5;155m Ex: word1\x1b[1;38;5;255m;\x1b[0m\x1b[30;38;5;155mword2 \x1b[0m
____________________________________________
"""))
    fileSavePath=input("[\x1b[30;38;5;155m+\x1b[0m]\x1b[1;38;5;249m Enter the file name to save [default]:\x1b[1;38;5;249mpasslist.txt \x1b[0m\x1b[1;38;5;249m : \x1b[0m") or "passlist.txt"
    uporno=input("[\x1b[30;38;5;155m+\x1b[0m]\x1b[1;38;5;68m upper or lower?\x1b[1;38;5;255m Or hit enter for lower : \x1b[0m") or "lower"
    list_inputs=list(input("[\x1b[30;38;5;155m+\x1b[0m]\x1b[30;38;5;240m Enter the words and use '\x1b[1;38;5;255m;\x1b[0m\x1b[30;38;5;240m' between : \x1b[0m").strip().split(';'))
    if uporno == 'upper':
        upper(list_inputs,fileSavePath)
    if uporno == 'lower':
        lower(list_inputs,fileSavePath)
if __name__ == '__main__':
    main()
