import os

fin = open("stations.txt").read().splitlines()

for i in fin:
	os.system("wget https://tidesandcurrents.noaa.gov/sltrends/downloadMeanSeaLevelTrendsCSV.htm?stnid=" + i)
