


import logRegres
from numpy import *
import csv
f0=csv.reader(open("results.csv","r"))
out = open("results0.csv", "a", newline="")
csv_write = csv.writer(out, dialect="excel")
results=[]
results0=[[""]*2 for  i in range(418)]
for res in f0:
    results.append(res  )
for i in range(len(results)):
    results0[i][0]=str(892+i)
    results0[i][1]=str(results[i][0])
for i in range(len(results0)):
    csv_write.writerow(results0[i])

print(results0)
print(results)
print(len(results))
print(len(results0))
