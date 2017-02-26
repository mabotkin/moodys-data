from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt
fin = open("../data/predictionForSeaLevels.txt").read().splitlines()

CLUSTERS = 3
ITERATIONS = 10000

ten = []
twenty = []
fifty = []
hundred = []

ten_clusters = [[],[],[]]
twenty_clusters = [[],[],[]]
fifty_clusters = [[],[],[]]
hundred_clusters = [[],[],[]]

for k in fin:
	i = k.split()
	station = i[0]
	a = float(i[1])
	b = float(i[2])
	c = float(i[3])
	d = float(i[4])
	ten.append(a)
	twenty.append(b)
	fifty.append(c)
	hundred.append(d)

a = kmeans2(ten,CLUSTERS,iter=ITERATIONS)
b = kmeans2(twenty,CLUSTERS,iter=ITERATIONS)
c = kmeans2(fifty,CLUSTERS,iter=ITERATIONS)
d = kmeans2(hundred,CLUSTERS,iter=ITERATIONS)

for i in range(len(a[1])):
	ten_clusters[a[1][i]].append(ten[i])
for i in range(len(b[1])):
	twenty_clusters[b[1][i]].append(twenty[i])
for i in range(len(c[1])):
	fifty_clusters[c[1][i]].append(fifty[i])
for i in range(len(d[1])):
	hundred_clusters[d[1][i]].append(hundred[i])

fout = open("../data/clusters.txt","w")
fout.write("TEN_YEAR:\n")
for i in range(CLUSTERS):
	fout.write("CLUSTER " + str(i) + ":\n")
	fout.write("MEAN: " + str(a[0][i]) + "\n")
	for j in ten_clusters[i]:
		fout.write(str(j) + "\n")
fout.write("TWENTY_YEAR:\n")
for i in range(CLUSTERS):
	fout.write("CLUSTER " + str(i) + ":\n")
	fout.write("MEAN: " + str(a[0][i]) + "\n")
	for j in twenty_clusters[i]:
		fout.write(str(j) + "\n")
fout.write("FIFTY_YEAR:\n")
for i in range(CLUSTERS):
	fout.write("CLUSTER " + str(i) + ":\n")
	fout.write("MEAN: " + str(a[0][i]) + "\n")
	for j in fifty_clusters[i]:
		fout.write(str(j) + "\n")
fout.write("HUNDRED_YEAR:\n")
for i in range(CLUSTERS):
	fout.write("CLUSTER " + str(i) + ":\n")
	fout.write("MEAN: " + str(a[0][i]) + "\n")
	for j in hundred_clusters[i]:
		fout.write(str(j) + "\n")
fout.close()
