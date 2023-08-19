import zipfile
import sys
import os

platform_infos = [
    {'platform_name': 'vita', 
     'input_file_name': 'vita_games_without_dlc.txt',    
     'output_folder': 'r:\\ROMS-1G1R\\erista-nointro-sony-playstation-vita-psn-content',
    },
    # {'platform_name': 'wii', 
    #  'word_to_append': 'https://myrient.erista.me/files/Redump/Nintendo - Wii - NKit RVZ [zstd-19-128k]/',
    #  'output_file_name': 'wii-myrient-links-1g1r.txt'
    # },    
]

def create_empty_zip_files(base_dir, file_name):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Folder '{base_dir}' created.")
    else:
        print(f"Folder '{base_dir}' already exists.")

    with open(file_name, 'r') as file:
        zip_file_names = file.read().splitlines()

    for name in zip_file_names:
        name = os.path.join(base_dir, name)
        print("name = %s" % name)
        with zipfile.ZipFile(name, 'w') as zip_file:
            pass

    print("-----------------------------------------------------")
    print("%d Empty zip files created!" % len(zip_file_names))
    print("-----------------------------------------------------")
    # print(f"Empty zip files created: {zip_file_names}")

def get_platform_info_by_name(platform_infos, name):
    for platform_info in platform_infos:
        if platform_info['platform_name'] == name:
            return platform_info
    return None

if len(sys.argv) < 1:
    print("Usage: python program.py <input_file> <output_file>")
    sys.exit(1)

platform_name = sys.argv[1]

print("Getting platform info for platform_name = %s" % platform_name)
platform_info = get_platform_info_by_name(platform_infos, platform_name)

# Example usage
base_dir = platform_info['output_folder']
txt_file_name = platform_info['input_file_name']

create_empty_zip_files(base_dir, txt_file_name)