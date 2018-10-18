import requests
import uuid
import os
from collections import namedtuple
import shutil
import time
import re
from PIL import Image

class Image_loader(object):
    """docstring for Image_loader"""
    def __init__(self):
        self.image_dir_path = os.path.join('source','images')
        self.post_dir_path = os.path.join('source','_posts')
        self.wait_to_rewrite = False
        self.rewrite_time = 0

    def is_valid_image(self,filename):
        valid = True
        try:
            Image.open(filename).load()
        except OSError:
            valid = False
        return valid
    def down_load_image(self,image_url,image_type):
        flag = True
        i = 0
        # 如果图片不完整就删除重新下载
        while flag:
            # os.remove(image_path)
            response = requests.get(image_url)

            loading = '.'*(i+1)
            print('File check:' + loading , end='\r')
            i += 1

            self.image_name = uuid.uuid4().hex + '.' + image_type
            image_path = os.path.join(self.image_dir_path,self.image_name)

            with open (image_path,'wb') as file:
                file.write(response.content)
            flag = not self.is_valid_image(image_path)
            if flag:
              os.remove(image_path)

        loading = loading.replace('.',' ')
        print('File check: √' + loading)
        print('download ok: ' + image_path)

    def get_file_list(self,dir_path = '.',file_types = '.*'):

        File_data = namedtuple('File_data',['file_name','file_path','file_type'])
        result_list = []
        dir_path = os.path.abspath(dir_path)
        file_data_list = [File_data(file_name,os.path.join(dir_path,file_name),os.path.splitext(file_name)[1]) for file_name in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,file_name))]
        if file_types == '.*':
            return file_data_list
        file_data_list = [File_data(file_name,file_path,file_type) for file_name,file_path,file_type in file_data_list if file_type and file_type in file_types]
        return file_data_list


    def rewrite_image(self):

        file_list = self.get_file_list(self.post_dir_path,'.md')
        for file_data in file_list:
            file_text = ''

            print('rewrite:' + file_data.file_path)
            with open(file_data.file_path,'r',encoding = 'utf-8') as file:
                for line in file:
                    matched = re.compile(r'!\[(.*?)\]\((http.*?)\)').match(line)
                    if matched:
                        self.wait_to_rewrite = True
                        # 处理查询： ![x](https://cdn.sspai.com/minja/2018.jpg?imageView1)'
                        if re.search(r'\?',line):
                            image_url = matched.group(2).split('?')[0]
                        else:
                            image_url = matched.group(2)
                        image_type = image_url.split('.')[-1]
                        if image_type not in ['bmp','jpg','png','tif','gif','pcx','tga','exif','fpx','svg','psd','cdr','pcd','dxf','ufo','eps','ai','raw','WMF','webp']:
                            image_type = 'png'
                        print(line)
                        print(image_url)
                        self.down_load_image(image_url,image_type)
                        line = '![{0}](/images/{1})'.format(matched.group(1),self.image_name)
                        print(line)
                    file_text += line

            # 如果有网络图片，重写文件
            if self.wait_to_rewrite == True:
                file_bak = file_data.file_path + '.bak'
                print(file_data.file_path)
                shutil.copy(file_data.file_path,file_bak)
                with open(file_data.file_path,'w',encoding = 'utf-8') as file:
                    file.write(file_text)
                os.remove(file_bak)
                self.wait_to_rewrite == False
                self.rewrite_time += 1
        print('一共重写了 {} 个文件，并将图片下载到了本地'.format(self.rewrite_time))

image_loader = Image_loader()
image_loader.rewrite_image()
