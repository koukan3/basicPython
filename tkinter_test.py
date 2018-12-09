#coding: utf-8

from tkinter import *
import os  

def write():
	textVar.set("")
	text.delete("0.0","end")
	label.config(text = "写日记模式")
	listBox.pack_forget()
	entry.pack()
	text.pack()

def read():
    listBox.delete(0,END)
    dir = os.getcwd()
    list = os.listdir(dir)

    showText = "看日记模式"
    if len(list)==0:
    	showText += "(日记本是空的)"
    label.config(text = showText)

    for item in list:
    	listBox.insert(0,item)

    listBox.bind('<Double-Button-1>',"showDiary")

    entry.pack_forget()
    text.pack_forget()
    listBox.pack()

def showdiary(event):
	print(listBox.curselection())
	title = listBox.get(listBox.curselection())
	showTitle = title[:-4]
	textVar.set(showTitle)

	fileObj = open(title, "r+")
	content = fileObj.read();
	text.delete("0.0","end")
	text.insert("end",content)
	fileObj.colse()

	listBox.pack_forget()
	entry.pack()
	text.pack()

def save():
	title = textVar.get() + ".text"
	content = text.get("0.0","end")

	if title != ".txt":
		fileObj = open(title, "wb")
		fileObj.write(bytes(content,encoding='utf-8'));
		fileObj.close()
		label.config(text = "已保存")
	else:
		label.config(text = "请输入标题")

def initDiary():
	dir = os.getcwd()
	list = os.listdir(dir)
	haveDiary = False
	for item in list:
		if item == "diary":
			haveDiary = True
	if haveDiary == False:
		os.mkdir("diary")
	os.chdir("./diary")

initDiary()

root = Tk()
root.geometry('500x400')   
root.title("程序员日记本")  

saveBtn = Button(root, text="保存",command=save)
saveBtn.pack(side=LEFT, anchor='sw')

quitBtn = Button(root, text="退出",command=quit)
quitBtn.pack(side=RIGHT, anchor='se')

writeBtn = Button(root, text="写日记", command=write)
writeBtn.pack(side=BOTTOM, anchor='s')

readBtn = Button(root, text="看日记",command=read)
readBtn.pack(side=BOTTOM, anchor='s')

textVar = StringVar()
entry = Entry(root, textvariable=textVar)
text = Text(root)
listBox = Listbox(root, height = 300)

label = Label(root)
label.pack()

root.mainloop()        