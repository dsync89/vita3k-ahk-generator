"""
Generate a list with only Game Type, excluding DLC, Theme, Avatar, PCSE, PSCG ... .
Use the ROMs downloaded from 
"""
import os

folder_path = 'r:\\ROMS-1G1R\\erista-nointro-sony-playstation-vita-psn-content'  # Replace with the actual folder path
output_file = 'vita_games_without_dlc.txt'  # Name of the output file

# Get the list of files in the folder
files = os.listdir(folder_path)

# Filter files that exclude the words 'DLC' and 'theme'
filtered_files = [file for file in files if 'DLC' not in file and 'Theme' not in file and 'Avatar' not in file and 'PCSE' not in file and 'PCSG' not in file and 'Soundtrack' not in file]

# Save the filtered files to a text file
with open(output_file, 'w') as file:
    for filtered_file in filtered_files:
        file.write(filtered_file + '\n')

print("Filtered files saved to", output_file)