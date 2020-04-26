f  = open('output.txt')

my_dict = {"line_num":[],"left":[],"conf":[],"text":[]}
line = f.readline()
#print(line)
line = f.readline()
while line:
    line_split = line.split('\t')
    #print(line_split)
    my_dict["line_num"].append(int(line_split[4]))
    my_dict["left"].append(line_split[6])
    my_dict["conf"].append(line_split[10])
    my_dict["text"].append(line_split[11])
    line = f.readline()

f.close()
print(sorted(set(my_dict["line_num"])))
bucket_dict={}
for i in range(len(my_dict["line_num"])):
    if my_dict["line_num"][i] in bucket_dict:
        bucket_dict[my_dict["line_num"][i]].append(my_dict["text"][i].strip())
    else:
        bucket_dict[my_dict["line_num"][i]] = [my_dict["text"][i].strip()]

for key in bucket_dict:
    print(key, " --> ", bucket_dict[key])
