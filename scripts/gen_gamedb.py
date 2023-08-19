""" 
Generate a .gamedb.txt file that AHK script uses to lookup GameID from GameName.
Each row has the content of GAME_TITLE|GAME_ID
"""
import os

source_directory = "s:\\roms-staging\\vita pkg imported success"
output_file = ".gamedb.txt"

game_name_and_game_id_tuples = []

def read_filenames_from_file(filename):
    with open(filename, "r") as file:
        filenames = file.read().splitlines()
    return filenames

def extract_filenames_from_subfolders(parent_directory):
    for root, _, files in os.walk(parent_directory):
        for filename in files:
            game_title = os.path.basename(root)
            print("Game folder name:", game_title)
            print("Found filename:", filename)

            # Splitting the filename by '-' and '_'
            try:
                parts = filename.split('-')
                game_id = parts[1].split('_')[0]
            except:
                game_id = "?"

            print("Extracted game ID:", game_id)                

            game_name_and_game_id_tuples.append( (game_title, game_id))

def print_tuples(tuples):
    print("START COPY AND PASTE THESE TO .GAMEDB.TXT!")
    print("=======================================================")
    for game_title, game_id in game_name_and_game_id_tuples:    
        print("%s|%s" % (game_title, game_id))
    print("=======================================================")

def save_tuples_to_file(tuples, output_file):
    with open(output_file, "w") as file:
        for game_title, game_id in tuples:
            file.write("%s|%s\n" % (game_title, game_id))

def main():
    extract_filenames_from_subfolders(source_directory)
    print_tuples(game_name_and_game_id_tuples)
    save_tuples_to_file(game_name_and_game_id_tuples, output_file)

if __name__ == "__main__":
    main()

# EOF