import os
import pandas as pd
import numpy as np


class Fat(object):
    lis = []
    # lis_byte = [] # to store byte
    # constructor to initiate size for fat table

    def __init__(self, lis):
        self.lis = lis
        for i in range(0, 1024):
            i = 0  # mean available block
            lis.append(i)

    # creates our fattable in a type of data structure called Dataframes
    def initialize_fat(self):
        # to store as dictionary
        fatable = {
            "Next": pd.Series(self.lis)
        }
        # Our data frame variable carries the fattable
        df = pd.DataFrame(fatable)
        # 1 for superblock + 4 for fat_table
        for i in range(0, 5):  # In this block we put -1 in the first 5 index
            df["Next"][i] = -1
        # علشان يشاور عليه في اي فنكشن بعد كده
        self.df = df

    # Store in dataframe in file
    def write_Fatable(self):
        # before open  => int
        with open("os.txt", "rb+") as f:
            # after open => byte  (as section)
            f.seek(1024)  # mean skip superblock 1*1024 and i will write after it
            # convert list of int  TO   list of bytes
            f.write(self.df.to_string().encode())  # str() != .to_string (here)
            # print(self.df)  # for test

    # Get dataframe to use in other methods (as section)
    def get_Fatable(self):
        return self.df.to_string()

    # Print fat for debuging or testing (as section)
    def print_Fatable(self):
        print(self.get_Fatable())

    # get available block(just first block) in dataframe
    def get_available_block(self):
        for i in range(0, 1024):
            if self.df["Next"][i] == 0:
                print(i)  # print first index
                break

    # get count of all blocks from fat table (task in Dir_entry)
    def get_availble_blocks(self):
        count = 0
        for i in range(1024):
            if self.df["Next"][i] == 0:
                count = count + 1
        return count
    # get index's value

    # get value in fat table
    def get_next(self, index):
        print(self.df["Next"][index])

    # set value in your input of index
    def set_next(self, index, value):
        with open("os.txt", 'r+') as f:
            f.seek(1024)
            self.df["Next"][index] = value
            f.write(self.df.to_string())
