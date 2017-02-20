file_in = open("AmesHousing-test_set.txt",'r')
file_out = open("AmesHousing-test_set2.txt",'w')

header = file_in.readline()
file_out.write(header)

for line in file_in:
    line_splitted = line.split(' ')
    #index = [1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,22,23,24,25,26,28,29,30,31,32,33,34,36,40,41,42,43,54,56,58,59,61,64,65,66,73,74,75,79,80]
    #line_splitted = [i for j, i in enumerate(line_splitted) if j not in index]
    print(line_splitted)
    line_splitted = filter(lambda x: x != '', line_splitted)

    if len (line_splitted) == 37:
    	print(' '.join(line_splitted)) #Prints `[1, 2, 5, 6, 8, 9]`
    	file_out.write(' '.join(line_splitted))