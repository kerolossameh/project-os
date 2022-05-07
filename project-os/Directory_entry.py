from numpy import little_endian


class Directory_entry:
    # # size of name must = > 11 byte (mean 11 charactiers)
    # # 7 byte for name , 4 byte for extention
    # # size = 11 byte
    file_name = ''

    namelist = []

    # # 0x mean hixdicimal  0x0 (file)    or    0x10 (folder)
    # # size = 1 byte
    file_attr = ''
    file_extention = []

    # # have collection of zeros
    # size = 12 byte
    file_empty = b'000000000000'

    # # any size you will track  => 4 byte (mean number)
    file_size = 0

    # # first place ,we will store in it => 4 byte (mean number)
    first_cluster = []

    nameList = []
    attrlist = []
    # # ---- 11 + 12 + 4 + 4 + 1 = 32 byte (size of file) ----

    # Constractor to intiate from directory entry
    def __init__(self, file_name, file_attr, first_cluster):
        file_nameList = file_name.split('.')
        file_name = file_nameList[0][:7]
        self.nameList.append(file_name)

        if file_attr == b'0x0':
            file_attr = 'file'
        elif file_attr == b'0x10':
            file_attr = 'folder'
        self.file_extention.append(file_attr)

        self.first_cluster.append(first_cluster)

    def ckeck_type(self):
        # -------------- check type of attribute------
        if self.file_attr == b'0x0':  # This is a file
            # ---------- check size of file----------
            if len(self.file_name) >= 11:
                # in this if block we make a list contain the name of file and the extension
                # and we put each in variable
                file_nameList = self.file_name.split(".")
                file_name = file_nameList[0][:7]
                file_extension = file_nameList[1][:3]
                # sort
                self.nameList.append(file_name)
                self.attrlist.append(file_extension)

            else:
                # if user does not enter a long name we set the default value
                file_name = "Newfile.txt"
                file_nameList = file_name.split(".")
                file_name = file_nameList[0][:7]
                file_extension = file_nameList[1][:3]
                # sort
                self.nameList.append(file_name)
                self.attrlist.append(file_extension)
        elif self.file_attr == b'0x10':  # This is a folder
            # By slicing we take only letter before dot
            file_nameList = self.file_name.split(".")
            self.file_size = 0
            folder_name = file_nameList[0][:11]
            # sort
            self.nameList.append(folder_name)
            self.attrlist.append('folder')

    # take directory entry => return array of byte

    def get_bytes(self):
        # name,attr,size,firstcluster to bytes
        arr = bytearray(32)
        arr[0:10] = self.file_name.encode()
        arr[10:11] = self.file_attr
        arr[11:23] = self.file_empty
        arr[23:27] = bytes(self.file_size)
        arr[27:31] = bytes(self.first_cluster)
        return arr

    # take array of byte => return directory entry
    def get_dir_entry(self, arr_bytes):
        # how to convert bytearray to list
        l = []
        dir = Directory_entry()
        l.append(dir)
        name = arr_bytes[0:10].decode()
        l.append(name)
        attr = arr_bytes[10:11]
        l.append(attr)
        empty = arr_bytes[11:23]
        size = arr_bytes[23:27]
        f_cluster = arr_bytes[27:31]
        return l
