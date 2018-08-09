import requests
import uuid
import os
from collections import namedtuple
import shutil
import time
import re

class Image_loader(object):
    """docstring for Image_loader"""
    def __init__(self):
        self.image_dir_path = os.path.join('source','images')
        self.post_dir_path = os.path.join('source','_posts')
        self.wait_to_rewrite = False
        self.rewrite_time = 0

    def down_load_image(self,image_url):
        response = requests.get(image_url)
        self.image_name = uuid.uuid4().hex + '.png'
        image_path = os.path.join(self.image_dir_path,self.image_name)

        with open (image_path,'wb') as file:
            file.write(response.content)
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
                    matched = re.compile(r'!\[(.*?)\]\((http.*?\.png)\)').match(line)
                    if matched:
                        self.wait_to_rewrite = True
                        print(line)
                        print(matched.group(2))
                        self.down_load_image(matched.group(2))
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