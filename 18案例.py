#coding:utf-8
import numpy as np,os
import PIL.Image as Image #图片的工具库 == java 中java.awt
import pickle # pickle处理矩阵虚拟化和反虚拟化
# 把30 张图片变成矩阵，存储在一个文件，让后从这个文件把矩阵读取处理，还原成图片

class Image_Util:

    @staticmethod
    def image_to_array(dir):
        all_array=[]
        file_array=os.listdir(dir);
        for i in file_array:
            image_path=os.path.join(dir,i) #图片绝对路径
            image=Image.open(image_path) #内存中一个图片对象
            r,g,b=image.split() #把图片进行R,G,B分离
            r_array=np.array(r).reshape((62500,))
            g_array=np.array(g).reshape((62500,))
            b_array=np.array(b).reshape((62500,))
            image_array=np.hstack((r_array,g_array,b_array)) #整个矩阵就是一行，代表一个图片
            all_array=np.concatenate((all_array,image_array))
        all_array=all_array.reshape((len(file_array),62500*3)) # 整个矩阵中有多行(图片个数),每一行代表一张图片
        b_f=open("image.bat","wb") #准备一个二进制文件，写入矩阵
        pickle.dump(all_array,b_f)
        b_f.close()

    @staticmethod
    def read_array_to_image(file):
        f=open(file,"rb")
        all_array=pickle.load(f)
        print(all_array.shape)
        image_count=all_array.shape[0];
        all_array=all_array.reshape((image_count,3,250,250))
        for i in range(0,image_count):
            r=Image.fromarray(all_array[i][0]).convert("L")
            g=Image.fromarray(all_array[i][1]).convert("L")
            b=Image.fromarray(all_array[i][2]).convert("L")
            image=Image.merge("RGB",(r,g,b))
            # image.show()
            image.save("result/%d.jpg"%i,"jpeg")
if __name__=='__main__':
    # Image_Util.image_to_array("images")
    Image_Util.read_array_to_image("image.bat")