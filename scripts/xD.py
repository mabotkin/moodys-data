import re
fin = open("data.htm").read()

#a = re.compile("<u>(\d{7})</u>\s</a></td>\s*/s*<td id=\"stationtablecontent\">(\w*)</td>\s*<td id=\"stationtablecontent\">(\w*)</td>")
a = re.compile("\d{7}")
x = a.findall(fin)

fout = open("stations.txt","w")

for i in x:
	fout.write(str(i) + "\n")

fout.close()
