#
# Rename files
#
import os
def rename_files():
    # get file from folder
    file_list = os.listdir("/Users/Sneha/Documents/jobs/Python projects udacity/prank")
    print(file_list)
    
    saved_path = os.getcwd()
    print("Current working directory: "+saved_path)
    
    os.chdir("/Users/Sneha/Documents/jobs/Python projects udacity/prank")
    
    for file_name in file_list:
        print("Old filename: "+file_name)
        print("New filename: "+file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
    
    os.chdir(saved_path)    
    
rename_files()