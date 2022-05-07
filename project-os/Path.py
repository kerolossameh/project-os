import os


class Path:
    def getpath():
        path = print(os.getcwd(), ">")  # This function gets the path

    def helpfunc(args):
        if (len(args) == 1):  # this function prints avalible commands
            print("cd - change directory")
            print("cls - clear the screen")
            print("quit -  exit the program")
            print("dir - List the contents of directory .")
            print("copy - Copies one or more files to another location")
            print("del - Deletes one or more files.")
            print("help -Provides Help information for commands")
            print("md - Creates a directory.")
            print("rd - Removes a directory.")
            print("rename - Renames a file.")
            print("type - Displays the contents of a text file")
            print("import - import text file(s) from your computer.")
            print("export - export text file(s) to your computer.")
        elif(len(args) != 2):
            print("determine a command name ")
        elif(args[1] == "cls"):
            print("cls : clear the screen")
        elif(args[1] == "cd"):
            print("cd : change Folder")
        elif(args[1] == "quit"):
            print("quit : exit the program")
        elif(args[1] == "dir"):
            print("dir - List the contents of Folder ")
        elif(args[1] == "copy"):
            print("copy - Copies one or more files to another location")
        elif(args[1] == "del"):
            print("del - Deletes one or more files")
        elif(args[1] == "md"):
            print("md - Creates a Folder")
        elif(args[1] == "rd"):
            print("rd - Removes a Folder")
        elif(args[1] == "rename"):
            print("rename - Renames a Folder")
        elif(args[1] == "mf"):
            print("mf - Create a File")

    def check_command():
        while True:
            Path.getpath()
            command = input().lower()  # Take input from user # cls cls
            args = command.split(" ")  # ['cls','cls]
            command = args[0]
            commands = ["cls", "quit", "cd", "dir", "copy",
                        "del", "md", "rd", "rename", "type", "mf"]
            # In this  if-else block we check out the command
            if(command == 'cls'):  # Printing valid if the command exists'
                os.system('cls')
            elif(command == "quit"):  # Exit Program wheen user types quit
                os._exit(0)
            elif (command == "help"):
                Path.helpfunc(args)

            elif (command == 'md'):
                path = os.getcwd()
                name = args[1]
                path_name_folder = f'{path}\\{name}'
                try:
                    if name in os.listdir(path):
                        # print(all)
                        print("Folder Exists")
                    else:
                        os.mkdir(path_name_folder)
                        print("Has Maked")
                except ValueError as ve:
                    print(ve)
            # make file
            elif (command == 'mf'):
                path = os.getcwd()
                name = args[1]
                # path_name = f'{path}\\{name}'
                try:
                    if name in os.listdir(path):
                        # print(all)
                        print("File Exists")
                    else:
                        open(name, 'w')
                        print("Has Maked")
                except:
                    print('Please, ensure your input')

            # remove dir
            elif (command == 'rd'):
                path1 = os.getcwd()
                name1 = args[1]
                path_name = f'{path1}\\{name1}'
                has_files = os.listdir(path_name)
                try:
                    if name1 in os.listdir(path):
                        if len(has_files) == 0:
                            os.rmdir(path_name)
                            print("Has Removed")
                        else:
                            yes = input(
                                "if you want remove all in it prase, y : ")
                            if(yes == 'y' or 'yes'):
                                for files in has_files:
                                    new_all = f'{path_name}\\{files}'
                                    os.remove(new_all)
                                os.rmdir(path_name)
                    else:
                        print("Folder not exists")
                except:
                    print('Please, Ensure Folder is Empty')

            # rename file or folder
            elif (command == 'rename'):
                path = os.getcwd()
                try:
                    if os.path.exists(path):
                        old_name = args[1]
                        new_name = args[2]
                        os.rename(old_name, new_name)
                        print('Has Renamed')
                    else:
                        print("The directory does not exist")
                except:
                    print('Please, ensure your input')

            elif (command == 'cd'):
                path = args[1]
                try:
                    os.chdir(path)
                    print("Current working directory: {0}".format(os.getcwd()))
                except FileNotFoundError:
                    print("Directory: {0} does not exist".format(path))
                except NotADirectoryError:
                    print("{0} is not a directory".format(path))
                except PermissionError:
                    print(
                        "You do not have permissions to change to {0}".format(path))

            elif (command == 'dir'):
                path = os.getcwd()
                print(os.listdir(path))

            elif (command == 'del'):
                file = args[1]
                if os.path.exists(file):
                    os.remove(file)
                else:
                    print("The file does not exist")

            elif(command in commands):
                print("Valid")

            else:  # if command not avalible print invalid
                print(f" {command} command is invalid")
