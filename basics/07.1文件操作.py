#coding:utf-8

# f=open(r"D:\test.file","r") #字符串前面的r代表禁用转义
# out=open("D:\\copy.file",'w')
# # print(f.read())
# out.write(f.read())
# f.close()
# out.close()

import os

def rename_path(file):
    if os.path.isdir(file):
        fs=os.listdir(file)
        for f in fs:
            rename_path(os.path.join(file,f))
    else:
        source_file_name=os.path.basename(file)
        if source_file_name.endswith(".pdf"):
            new_file_name=source_file_name[:source_file_name.rfind(".pdf")]+"_backup"+".pdf"
            new_file_path=os.path.join(os.path.dirname(file),new_file_name)
            os.rename(file,new_file_path)
rename_path(r"D:\shell")

fs=os.listdir(r"D:\shell")
for f in fs:
    print(f)
