import os
import shutil
import argparse

#fonction for list files and directories in path of your choice
def list_dir(location) :
    directory = os.listdir(location)
    for file in directory :
        print(f'{file}')

#fonction for rename files            
def rename_file(location, file, new_file) :
    os.rename(location + file, location + new_file)  

#fonction for create list of file
def enumerate_files(location) :
    directory = os.listdir(location)
    os.chdir(location)
    for i, file in enumerate(directory, start=0) :
        if os.path.isfile(file) == True:
            os.rename(file, str(i) + "_" + file)

#fonction for zip files
def zip_files(location, destination) :
    shutil.make_archive(location, 'zip', destination)

#fonction for sort files
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

#fonction for remove filenames spaces           
def remove_filename_space(location) :
    directory = os.listdir(location)
    os.chdir(location)
    for file in directory :
        filename = file.replace(' ', '_')
        os.rename(file, filename)
        print(f'{filename}')
    
    
#add argparse argument
parser = argparse.ArgumentParser(description="Rename your files")
parser.add_argument("-l", "--location", required="true",type=str, help="Location of directories and files")
parser.add_argument("-f", "--file", type=str, help="Choice of your file")
parser.add_argument("-nf","--new_file", type=str, help="Name of the new file")
parser.add_argument("-d", "--destination", type=str, help="Destination of directories and files")
parser.add_argument("-s", "--sort_file", action='store_true', help="Sort files in different directories")
parser.add_argument("-ld", "--list_directory", action='store_true', help="List files and directories")
parser.add_argument("-ed", "--enumerate_directory", action='store_true', help="Create list of files")
parser.add_argument("-rs", "--remove_space", action='store_true', help="Remove filename space")
parser.add_argument("-z","--zip", action='store_true', help="Zip a directory")
args = parser.parse_args()

#Call the fonction for list dir with -ld argument
if args.location and args.list_directory :
    list_dir(args.location)

#Call the fonction for rename file with -f and -nf arguments
elif args.location and args.file and args.new_file :    
    rename_file(args.location, args.file, args.new_file)

#Call the fonction for add a number in front of the file name to create a list
elif args.location and args.enumerate_directory :
    enumerate_files(args.location)
    
#Call the fonction for ZIP files
elif args.location and args.zip and args.destination :
    zip_files(args.location, args.destination) 

#Call the fonction for sorts files
elif args.location and args.sort_file :
    sort_files(args.location)
    
#Call the fonction for remove filenames spaces
elif args.location and args.remove_space :
    remove_filename_space(args.location)