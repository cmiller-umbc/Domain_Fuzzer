import os

with open("domains.txt") as domains:
    content_list = domains.readlines()

    for i in range(len(content_list)):
        content_list[i] = str(content_list[i])
        content_list[i] = content_list[i].replace('\n','')

    x=0
    while x<len(content_list):
        cmd = "wget -q -O - -U demo http://"+content_list[x]+" --header \"Host: domainfronter.pages.dev\""
        res = os.system(cmd)
        print(res)
        x+=1