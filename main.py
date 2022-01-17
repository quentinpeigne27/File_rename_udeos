import os
import argparse

def list_dir(list_directory) :
        directory = os.listdir(list_directory)
        for file in directory :
            print(file)
            
def rename_file(file, new_file) :
        os.rename(file, new_file)  
            
def change_extension(file ,extension, new_extension) :
        file.replace(extension, new_extension)
        
def rename_files(list_directory, )
parser = argparse.ArgumentParser(description="Rename your files")
parser.add_argument("-d", "--directory", type=str, help="Choice of Target path")
parser.add_argument("-ld", "--list_directory", type=str, help="List directories and files")
parser.add_argument("-f", "--file", type=str, help="Choice of your file")
parser.add_argument("-nf","--new_file", type=str, help="Name of the new file")
parser.add_argument("-e","--extension", type=str, help="Files extension")
parser.add_argument("-ne","--new_extension", type=str, help="Change files extension")
args = parser.parse_args()

if args.list_directory :
    list_dir(args.list_directory)
    
elif args.file and args.new_file :    
    rename_file(args.file, args.new_file)
        
elif args.file and args.extension and args.new_extension :
    change_extension(args.file, args.extension, args.new_extension)
        
    

                      
