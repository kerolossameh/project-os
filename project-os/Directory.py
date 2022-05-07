from asyncio.windows_events import NULL
from Directory_entry import *
from VirtualDisk import *
import pandas as pd
from Fat import *


class Directory(Directory_entry):
    dirlist = []

    # Constractor to intiate from directory entry
    def __init__(self, file_name, file_attr, first_cluster=0):
        super().__init__(file_name, file_attr, first_cluster)
        self.parent = Directory()

    # Sort info of directory as table
    def dir_table(self):
        data_entry = {
            'Name': pd.Series(self.nameList),
            'Attribute': pd.Series(self.file_extention),
            'First_cluster': pd.Series(self.first_cluster)
        }
        df = pd.DataFrame(data_entry)
        return df

    # Sort info of directory as table of bytes
    def sort_data_entry_as_byte(self):
        data_entry_byte = {
            'Name': pd.Series([str.encode(i) for i in self.nameList]),
            'Attribute': pd.Series(self.file_extention),
            'First_cluster': pd.Series(self.first_cluster)
        }
        df_byte = pd.DataFrame(data_entry_byte)
        return df_byte

    # write directory in virtual Disk
    def write_dir(self):
        # store 32 / size in dirsorfilesBYTES
        self.dirsorfilesBYTES = bytes(
            bytearray([None for _ in range(len(self.file_size)*32)]))
        # store dirsorfilesBYTES as array of bytes
        self.bytesList = bytearray(self.dirsorfilesBYTES)
        clusterFATindex = None
        
        if self.first_cluster != 0:
            clusterFATindex = self.first_cluster  # 6
        else:
            clusterFATindex = Fat.get_available_block()
            self.first_cluster = clusterFATindex
        lastCluster = -1  # 5 6 10 -1
        for i in range(len(self.bytesList)):
            if clusterFATindex != -1:  # 6
                VirtualDisk.write_block(clusterFATindex, self.bytesList[i])
                Fat.set_next(clusterFATindex, -1)  # full
                if lastCluster != -1:
                    Fat.set_next(lastCluster, clusterFATindex)
                    lastCluster = clusterFATindex  # 6
                    clusterFATindex = Fat.get_available_block()
        if self.parent != NULL:
            self.parent.update_content(self.dir_table())  # error
            self.parent.write_dir()
        Fat.write_Fatable()

    # read directory as table
    def read_dir(self):
        return self.dir_table()

    # take file name => return where (mean return index in dataframe)
    # if not exists => -1
    # if exits => index
    def search_dir(self, file_name):
        list_name = []
        index = -1
        df = self.read_dir()
        for name in df['Name']:
            list_name.append(name)
            if name == file_name:
                index = list_name.index(file_name)
        if index != -1:
            return index
        else:
            return index

    # return list of names from directory table
    def read_file_name(self):  # =>
        list_name = []
        df = self.read_dir()  # df
        for name in df['Name']:
            list_name.append(name)
        return list_name

    # def update_content(self , old = Directory_entry() ,new_file_name):
    #     df = self.read_dir()  # df
    #     # list_name = self.read_file_name()  # list of name
    #     index = self.search_dir(old_file_name)
    #     if index != -1:
    #         df['Name'].pop(index)
    #         df['Name'].add_prefix()

    # update from old record to new record in data frame
    def update_content(self, old, new):
        df = self.read_dir()  # df
        list_name = self.read_file_name()  # list of name
        index = self.search_dir(old)
        if index != -1:
            df.drop(index=index)
            df.append(old, new)

    # To clear directory size from all index cluster of fat by first_cluster
    def clearDirSize(self):
        clusterIndex = self.first_cluster
        next = Fat.get_next(clusterIndex)
        if clusterIndex == 5 and next == 0:
            return NULL
        while clusterIndex != -1:
            temp = clusterIndex
            clusterIndex = next
            Fat.set_next(clusterIndex, 0)
            if clusterIndex != -1:
                next = Fat.get_next(clusterIndex)

    # delete dir and parent , and edit in fat table
    def delete(self):
        self.clearDirSize()
        if Directory() == self:
            if self.parent != NULL:
                Directory.parent = self.parent
                Directory.read_dir()
        Fat.write_Fatable()
