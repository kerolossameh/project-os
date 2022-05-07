from Fat import *
from VirtualDisk import *
from Directory_entry import *
from Directory import *
from Path import *


def main():

    data = '''*dfdsgasdfasdfasdfasdsdzrfhsrjtkuliyrkutdrhst
gearwrhetjryfdfhbrhjgkhlgjhgsfdhgjh,ggjhfj,fghzdhfgjfhgs
dfgtdelkhmbedm;lkbthdnsdfmblk;rdgb,ndlf;thndsfbsdfbsfdbssfn
sdfmbldk;fgbkdg;lhmndgfbkldfn,gbdgl;ngd;hnsgcbvffxgbsfnsfn
sdfmklbdfngld;fmndgndghlkmngdhnglhn;lsdfdfgvsxfvbfxcgbszrb
gsdflkmsfgbdfngsdf',sdfgsdfg;lmsdfgaldfglmmsdflmsgddfvgfxdgbf
sdgsdlkfgsdflgsdfmlfngdngdfbls;df,'gmienokmfalsv;df'aopgif
fbk;lsmgdfsmsvkndsbgdmfl;mkbdoigegspflm;kdbgonfmsl;kbgsnm
sdfdsgasdfasdfasdfasdsdzrfhsrjtkuliyrkutdrhstgearwrhetjry
fdfhbrhjgkhlgjhgsfdhgjh,ggjhfj,fghzdhfgjfhgsfnbffxcnsnsng
dfgtdelkhmbedm;lkbthdnsdfmblk;rdgb,ndlf;thndsfbsdfbsfdbssfn
sdfmbldk;fgbkdg;lhmndgfbkldfn,gbdgl;ngd;hnsgcbvffxgbsfnsfn
sdfmklbdfngld;fmndgndghlkmngdhnglhn;lsdfdfgvsxfvbfxcgbszrb
gsdflkmsfgbdfngsdf',sdfgsdfg;lmsdfgaldfglmmsdflmsgddfvgfxdgbf
sdgsdlkfgsdflgsdfmlfngdngdfbls;df,'gmienokmfalsv;df'aopgif
fbk;lsmgdfsmsvkndsbgdmfl;mkbdoigegspflm;kdbgonfmsl;kbgsnm
sdfdsgasdfasdfasdfasdsdzrfhsrjtkuliyrkutdrhstgearwrhetjry
asedgsfhhffnbffxcnsnsngdgfghfg85*615xdcvd1'''

    # print(data[1])
    # print(len(data))

    VirtualDisk.initialize_file()
    VirtualDisk.write_block(data, 10)
    # VirtualDisk.get_block(10)

    lis = []  # list to Reserving Metadata(FAT table)
    test = Fat(lis)
    test.initialize_fat()
    test.write_Fatable()
    # test.print_Fatable()
    # test.set_next(5,10)
    # test.get_available_block(),# 6
    # test.get_next(5) # 10
    # test.get_availble_blocks()

    # dir = Directory(
    #     file_name='mina.txt',
    #     file_attr=b'0x0',
    #     first_cluster=0
    # )
    # dir1 = Directory(
    #     file_name='kero.txt',
    #     file_attr=b'0x0',
    #     first_cluster=8
    # )
    # dir2 = Directory(
    #     file_name='wesa.txt',
    #     file_attr=b'0x10',
    #     first_cluster=10
    # )

    # dir.ckeck_type()
    # print(dir.dir_table())
    # print(dir.sort_data_entry_as_byte())
    # dir.search_dir('wesa')
    # dir.update_content(
    #     old=Directory_entry(
    #         'mina.txt', b'0x0', 23
    #     ),
    #     new=Directory_entry(
    #         'test2.txt',b'0x10',53
    #     )
    # )
    # print(dir.dir_table())
    # print(dir.read_file_name())

    Path.check_command()


if __name__ == "__main__":
    main()
