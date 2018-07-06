# -*-encoding:utf-8-*-
# convert the files in the directory

import os, sys
path = sys.argv[1]
videos = []
for p,d,c in os.walk(path):
	for i in c:
		videos.append(os.path.join(path, i))

for video in videos:
	os.system('python3 middle.py ' + video)
