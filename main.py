import os
import shutil
import argparse

#fonction for list files and directories in path of your choice
def list_dir(list_directory) :
    directory = os.listdir(list_directory)
    for file in directory :
        print(file)

#fonction for rename files            
def rename_file(file, new_file) :
    os.rename(file, new_file)  

#fonction for create list of file
def enumerate_files(enumerate_directory) :
    directory = os.listdir(enumerate_directory)
    os.chdir(enumerate_directory)
    for i, file in enumerate(directory, start=1) :
        os.rename(file, str(i) + "_" + file)

#fonction for zip files
def zip_files(zip, directory) :
    shutil.make_archive(zip, 'zip', directory)

def sort_files(location) :
    directory = os.listdir(location)
    os.chdir(location)
    for file in directory :
        if ".pdf" in file :
            os.mkdir(location + "pdf")
            shutil.move(file, location + "pdf")
        elif ".png" in file :
            os.mkdir(location + "png")
            shutil.move(file, location + "png")
        elif ".txt" in file :
            os.mkdir(location + "txt")
            shutil.move(file, location + "txt")
        elif ".jpg" in file :
            os.mkdir(location + "jpg")
            shutil.move(file, location + "jpg")
        else :
            print("No such file ! Please read the README :)")
    
#add argparse argument
parser = argparse.ArgumentParser(description="Rename your files")
parser.add_argument("-d", "--destination", type=str, help="List directories and files")
parser.add_argument("-l", "--location", type=str, help="List directories and files")
parser.add_argument("-ed", "--enumerate_directory", type=str, help="List directories and files")
parser.add_argument("-s", "--sort_file", action='store_true', help="List directories and files")
parser.add_argument("-ld", "--list_directory", type=str, help="List directories and files")
parser.add_argument("-f", "--file", type=str, help="Choice of your file")
parser.add_argument("-nf","--new_file", type=str, help="Name of the new file")
parser.add_argument("-z","--zip", type=str, help="Name of the new file")
args = parser.parse_args()

#List dir with -ld argument
if args.list_directory :
    list_dir(args.list_directory)

#rename file with -f and -nf arguments
elif args.file and args.new_file :    
    rename_file(args.file, args.new_file)

#Add a number in front of the file name to create a list
elif args.enumerate_directory :
    enumerate_files(args.enumerate_directory)
    
#ZIP file
elif args.zip and args.directory :
    zip_files(args.zip, args.directory) 
    
elif args.sort_file :
    sort_files(args.location)