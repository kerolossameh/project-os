import pandas as pd
import numpy as np


class VirtualDisk(object):

    def initialize_file():
        with open("os.txt", 'w') as f:
            # Reserving super block  [1 * 1024]
            for i in range(1024):
                f.write('0')
            # Reserving Metadata(FAT table) block  [super + fat]
            for i in range(1024, 5*1024):
                f.write('*')
            # Reserving datafile  [super + fat + datafile]
            for i in range(5*1024, 1024*1024):
                f.write('#')

    # !!!!!!!!!!
    # write new block , will take list (mean data) , will take index (mean where i write data)
    def write_block(data, index):
        # here will write in file
        with open('os.txt', 'r+') as f:
            # f.seek((index+5) * 1024)  # 5 + 10
            f.seek((index+5) * 1024)
            # ignore numbers after comma
            # print(len(data))
            size_block = int(len(data) / 1024)
            # print(size_block)
            # cut and store
            new_data = ''.join(data[0:size_block * 1024])
            f.write(new_data)
        # print(len(new_data))

    '''
حته الاندكس مش قصده الاندكس بتاع الفات 
هو قصده الاندكس بتاع الداتا
و زي م احنا عرفين ان الفات دا الفهرس للداتا
ف هنشوف الفات الفاضي كفهرس علشان نبدا نكتب في المكان ده الداتا 
بس في منطقة الداتا (هي دي الي هنكتب فيها)
'''

    def get_block(index):
        data = ''
        with open("os.txt", 'r+') as f:
            data_from_file = f.read()
            skip_block = index + 5
            f.seek(skip_block * 1024)
            data = ''.join(
                data_from_file[skip_block*1024:(skip_block+1) * 1024])
            # with open('test.txt','w') as f :
            #     f.write(data)
        print(data)

    # def get_size_file():
    #     with open('os.txt', 'r+') as f:
    #         size = len(f.read())
    #         print(f"size of file = {size}")
