file_in = open("AmesHousing.txt",'r')
file_out = open("AmesHousing-clean.txt",'w')

header = file_in.readline()
file_out.write(header)

for line in file_in:
	line_splitted = line.split('\t')
	if not (line_splitted[14] == "Norm" and line_splitted[14] == "Norm"):
		continue
	if float(line_splitted[47]) > 1500:
		continue
	file_out.write(line)