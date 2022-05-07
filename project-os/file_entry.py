class File_entry:
    def __init__(self, file_name, file_attr, file_size, first_cluster):
        # if :
        self.file_name = file_name
        self.file_attr = file_attr
        self.file_size = file_size
        self.first_cluster = first_cluster
