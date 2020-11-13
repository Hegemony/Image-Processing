import glob

output_txt = 'list_attr_mydataset.txt'

for idx, f in enumerate(glob.glob('./my-processed-dataset/*.csv')):
# for idx, f in enumerate(glob.glob('./my-processed-dataset/result/*.csv')):
    print(f)
    with open(f, 'r') as csv_file:
        csv_file.readline()
        csv_list = csv_file.readline().split(', ')
        # print(csv_list[1])
        # if float(csv_list[1]) >= 0.88:
        # print(csv_list)
        if float(csv_list[1]) >= 0:
            # print(csv_list[1])
            aus = " ".join(csv_list[2:19])
            # open(output_txt, 'a').write(f.split('/')[-1].split('.')[0] + '.jpg ' + aus + '\n')  #linux写法
            open(output_txt, 'a').write(f.split('\\')[-1].split('.')[0] + '.jpg ' + aus + '\n')  # windows写法