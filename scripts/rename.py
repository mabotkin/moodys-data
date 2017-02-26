import os

for i in os.listdir("./"):
	print i
	if "download" in i:
		os.system("mv " + i + " " + i[-7:])
