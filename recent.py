f0=csv.reader(open("test.csv","r"))
f1=csv.reader(open("tri2.csv","r"))
f2=csv.reader(open("train1.csv","r"))
out=open("test0.csv","a",newline="")
out0=open("train0.csv","a",newline="")
out1=open("Cabin0,csv","a",newline="")
csv_write=csv.writer(out,dialect="excel")
csv_write1=csv.writer(out0,dialect="excel")

ticket=[]
cabin=[]
tri2=[]
test0=[]
train1=[]
for tra in f2:
    train1.append(tra)
for tri in f1:
    tri2.append(tri)
for tic in f0:
    test0.append(tic)
for i in range(len(test0)):
    for j in range(len(test0[i])):
        if test0[i][j]=="":
            test0[i][j]="0"
for i in range(len(test0)):

    if test0[i][3]=="male":
        test0[i][3]="0"
    else:
        test0[i][3]="1"
    if test0[i][10]=="S":
        test0[i][10]="0"
    if test0[i][10]=="Q":
        test0[i][10]="1"
    if test0[i][10]=="C":
        test0[i][10]="2"
    del(test0[i][2])
for i in range(len(tri2)):
    tri2[i][7]=tri2[i][0]
for i in range(len(test0)):
    test0[i][6]=test0[i][0]
dict={}
for i in range(len(train1)):
    dict.update({train1[i][9]:str(i)})
for i in range(len(test0)):
    test0[i][8]=dict.get(str(test0[i][8]),"0")

for i in range(len(tri2)):
    tri2[i][9]=dict.get(str(train1[i][9]),"0")
print(tri2)#9


for i in range(len(test0)):
    csv_write.writerow(test0[i])
for i in range(len(tri2)):
    csv_write1.writerow(tri2[i])
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
