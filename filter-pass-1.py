import csv

f10=[]
f11=[]

f20=[]
f21=[]

f30=[]
f31=[]

p10=[]
p11=[]
p12=[]

p20=[]
p21=[]
p22=[]
p23=[]

with open('1.csv') as f:
	fc = csv.reader(f,delimiter='\t')
	for row in fc:
		f10.append(row[0])
		f11.append(row[1])
f.close()

with open('2.csv') as f:
	fc = csv.reader(f,delimiter='\t')
	for row in fc:
		f20.append(row[0])
		f21.append(row[1])
f.close()

with open('3.csv') as f:
	fc = csv.reader(f,delimiter='\t')
	for row in fc:
		f30.append(row[0])
		f31.append(row[1])
f.close()

for i in range(len(f10)):
	for j in range(len(f20)):
		if f10[i] == f20[j]:
			p10.append(f10[i])
			p11.append(f11[i])
			p12.append(f21[j])

for i in range(len(p10)):
	for j in range(len(f30)):
		if p10[i] == f30[j]:
			p20.append(p10[i])
			p21.append(p11[i])
			p22.append(p12[i])
			p23.append(f31[j])

f = open('output.csv','w')
for i in range(len(p20)):
	f.write(str(p20[i]) + '\t' + str(p21[i]) + '\t' + str(p22[i]) + '\t' + str(p23[i]) + '\n')
f.close()

