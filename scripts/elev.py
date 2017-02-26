import requests
import re

fin = open("stations.txt").read().splitlines()
fout = open("../data/elevation.txt","w")

count = 1
for i in fin:
	r = requests.get("https://tidesandcurrents.noaa.gov/stationhome.html?id=" + i).text
	a = re.compile("<td>Met Site Elevation:</td>\s*<td>(.*)(?=</td>)")
	#print(a.findall(r)[0])
	fout.write(i + " " + a.findall(r)[0] + "\n")
	print(str(count) + "/" + str(len(fin)) + ": " + i)
	count += 1
fout.close()
