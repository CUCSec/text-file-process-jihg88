list=[]
with open('d:/Program Files/pywork/text-file-process-jihg88/log_files/201811113011.log','r',encoding='UTF-8') as f:
    for line in f:
        line1=line.split(',')
        line2=line1[1].split('：')
        list.append(line2[1])
        print(line2[1])
    print(list.count('201811113011'))


