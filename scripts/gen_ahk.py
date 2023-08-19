"""
Generate .AHK file for each game. The name of the .AHK file is based on the folder name from source dir.
"""
import os
import shutil

ahk_template_file = "./template.ahk"
source_directory = "s:\\roms-staging\\vita pkg imported success"
destination_directory = "./out"

def gen_ahk(source_file, dest_dir, filenames):
    for filename in filenames:
        dest_path = f"{dest_dir}/{filename}.ahk"
        
        shutil.copy(source_file, dest_path)
        
        print("File %s copied and renamed to %s" % (source_file, dest_path))

def main():
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    folder_list = [folder for folder in os.listdir(source_directory) if os.path.isdir(os.path.join(source_directory, folder))]

    gen_ahk(ahk_template_file, destination_directory, folder_list)

if __name__ == "__main__":
    main()

# EOF