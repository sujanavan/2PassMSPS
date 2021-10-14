import csv

f10=[]
f11=[]
f12=[]
f13=[]

f20=[]
f21=[]
f22=[]
f23=[]

f30=[]
f31=[]
f32=[]
f33=[]

p10=[]
p11=[]
p12=[]
p13=[]
p14=[]
p15=[]
p16=[]

p20=[]
p21=[]
p22=[]
p23=[]
p24=[]
p25=[]
p26=[]
p27=[]
p28=[]
p29=[]

with open('1.csv') as f:
	fc = csv.reader(f,delimiter='\t')
	for row in fc:
		f10.append(row[0])
		f11.append(row[1])
		f12.append(row[2])
		f13.append(row[3])
f.close()

with open('2.csv') as f:
	fc = csv.reader(f,delimiter='\t')
	for row in fc:
		f20.append(row[0])
		f21.append(row[1])
		f22.append(row[2])
		f23.append(row[3])
f.close()

with open('3.csv') as f:
	fc = csv.reader(f,delimiter='\t')
	for row in fc:
		f30.append(row[0])
		f31.append(row[1])
		f32.append(row[2])
		f33.append(row[3])
f.close()

for i in range(len(f10)):
	for j in range(len(f20)):
		if f10[i] == f20[j]:
			p10.append(f10[i])
			p11.append(f11[i])
			p12.append(f12[i])
			p13.append(f13[i])
			p14.append(f21[j])
			p15.append(f22[j])
			p16.append(f23[j])

for i in range(len(p10)):
	for j in range(len(f30)):
		if p10[i] == f30[j]:
			p20.append(p10[i])
			p21.append(p11[i])
			p22.append(p12[i])
			p23.append(p13[i])
			p24.append(p14[i])
			p25.append(p15[i])
			p26.append(p16[i])
			p27.append(f31[j])
			p28.append(f32[j])
			p29.append(f33[j])

f = open('output.csv','w')
for i in range(len(p20)):
	f.write(str(p20[i]) + '\t' + str(p21[i]) + '\t' + str(p22[i]) + '\t' + str(p23[i]) + '\t' + str(p24[i]) + '\t' + str(p25[i]) + '\t' + str(p26[i]) + '\t' + str(p27[i]) + '\t' + str(p28[i]) + '\t' + str(p29[i]) + '\n')
f.close()

