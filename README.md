# File_rename_udeos
***
This python script is a file renamer that works with argparse. It will allow you to :

* List the files and folders in a selected folder
* Rename a file
* Enumerate files to create a list
* Zip a folder of your choice 
* Classify file types into folders
* Remove spaces in filenames

You can get help with the command :

    python3 main.py -h
    
     optional arguments:
     
     -h, --help            Show this help message and exit
     -l LOCATION, --location LOCATION         Location of folders and files
     -f FILE, --file FILE         Choice of your file
     -nf NEW_FILE, --new_file NEW_FILE       Name of the new file
     -d DESTINATION, --destination      DESTINATION Destination of folders and files
     -s, --sort_file            Sort files in differents folders
     -ld, --list_directory        List files and folders
     -ed, --enumerate_directory       Create list of files
     -rs, --remove_space        Remove filename space
     -z, --zip             Zip folder

## List the files and folders in a selected folder

You can list files and folders, the command is :

    python3 main.py -l [The folder path of your choice] -ld
    
## Rename a file

You can rename a file, the command is :

    python3 main.py -l [The folder path of your choice] -f [Your filename] -nf [The new filename]
    
## Enumerate files to create a list

You can create a list, your files will be renamed with a number before the filename, the command is :

    python3 main.py -l [The folder path of your choice] -ed
    
## Zip a folder of your choice

You can zip a folder, the command is :

    python3 main.py -z -l [The folder path of your choice] -d [The destination path of your choice]
    
## Classify files types into folders

You can classify files (pdf, txt, png, jpg) into differents folders, the command is :

    python3 main.py -l [The folder path of your choice] -s

## Remove spaces in filenames

You can remove spaces in filenames, the command is :

    python3 main.py -l [The folder path of your choice] -rs
 


